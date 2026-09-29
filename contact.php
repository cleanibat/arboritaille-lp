<?php
// Formulaire de devis Arboritaille — envoi e-mail depuis le serveur + sauvegarde CSV hors docroot.
// Remplace FormSubmit (activation jamais cliquée, page d'erreur au lieu de la redirection).
date_default_timezone_set('Europe/Zurich');
mb_internal_encoding('UTF-8');

$DEST  = 'contact@arboritaille.ch, aymeric@cleanibat.fr'; // Robin + Aymeric, tous deux destinataires
$BCC   = 'aymeric@cleanibat.fr';                 // adresse utilisée seule pour les tests (?test=1)
$FROM  = 'Arboritaille <no-reply@arboritaille.ch>'; // domaine avec SPF Hostinger
$HOME  = dirname(dirname(dirname(__DIR__)));      // /home/uXXXXXXXXX
$CSV   = $HOME . '/leads_arboritaille.csv';
$TEST  = isset($_GET['test']) && $_GET['test'] === '1'; // test technique : envoi à la copie uniquement

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); header('Content-Type: text/plain; charset=UTF-8'); echo 'Methode non autorisee.'; exit; }
if (!empty($_POST['_honey'])) { header('Location: merci.html'); exit; }

function v($k){ return isset($_POST[$k]) ? trim(strip_tags((string)$_POST[$k])) : ''; }
$nom=v('Nom'); $tel=v('Téléphone'); $email=v('Email'); $ville=v('Localité'); $besoin=v('Besoin'); $msg=v('Message');
$src=v('Source'); $langue=v('Langue du client'); $sujet=v('Sujet'); $lp=preg_replace('/[^a-z0-9_-]/i','',v('lp')); $lang=v('lang')==='de'?'de':'fr';
$merci = ($lang==='de' ? 'de/danke.html' : 'merci.html') . '?lp=' . urlencode($lp);

if ($nom==='' || $tel==='' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  http_response_code(400); header('Content-Type: text/plain; charset=UTF-8');
  echo $lang==='de' ? 'Bitte prüfen Sie Name, Telefon und E-Mail.' : 'Merci de vérifier le nom, le téléphone et l\'e-mail.'; exit;
}

// 1) Filet de sécurité : le lead est écrit AVANT l'envoi de l'e-mail
$fh=@fopen($CSV,'a');
if($fh){ if(filesize($CSV)===0) fputcsv($fh,['date','nom','telephone','email','localite','besoin','message','source','langue','test','ip'],';');
  fputcsv($fh,[date('Y-m-d H:i:s'),$nom,$tel,$email,$ville,$besoin,str_replace(["\r","\n"],' ',$msg),$src,$langue,$TEST?'oui':'',$_SERVER['REMOTE_ADDR']??''],';');
  fclose($fh); @chmod($CSV,0600); }

// 2) E-mail
$subject = ($sujet!=='' ? $sujet : 'Nouvelle demande de devis – Arboritaille') . ($TEST ? ' [TEST]' : '');
$body  = ($TEST ? "*** TEST TECHNIQUE, à ignorer ***\n\n" : '');
$body .= "Nouvelle demande depuis page.arboritaille.ch\n\n";
$body .= "Nom        : $nom\nTéléphone  : $tel\nE-mail     : $email\nLocalité   : $ville\nBesoin     : $besoin\n";
if ($langue!=='') $body .= "Langue     : $langue\n";
$body .= "Page       : $src\n\nMessage :\n" . ($msg!=='' ? $msg : '(vide)') . "\n";
$headers  = "From: $FROM\r\nReply-To: $nom <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nX-Mailer: PHP/".phpversion();
$to = $TEST ? $BCC : $DEST;
@mail($to, '=?UTF-8?B?'.base64_encode($subject).'?=', $body, $headers);

// 3) Page de remerciement (le lead est déjà sauvegardé même si l'e-mail échoue)
header('Location: ' . $merci, true, 303);
exit;
