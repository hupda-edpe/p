<script>

if (typeof window.parent != 'undefined') {

<?php

/*----------------------------------********---------------------------------*/

if (isset( $_GET['ux'] )) {

    switch ($_GET['ux']) {

        case 'SIMPLIFIED':

        case 'SWITCHABLE':

        case 'SINGLE':

            $url = '../home';

            break;

        default:

            $url = 'casesListExtJs';

    }

} else if( key_exists('gmail', $_SESSION) && $_SESSION['gmail'] == 1 && !empty($enablePMGmail) && $enablePMGmail==1 ){

    $url = 'derivatedGmail';

} else {

    $url = 'casesListExtJs';

}

if (isset( $_GET['ux'] )) {

    echo 'if (typeof window.parent.ux_env != \'undefined\') {';

}

echo "  window.parent.location.href = '$url';";

if (isset( $_GET['ux'] )) {

    /*----------------------------------********---------------------------------*/

        echo '} else { window.parent.location.href = \'casesListExtJs\'; }';

    /*----------------------------------********---------------------------------*/

}

?>

}

</script>