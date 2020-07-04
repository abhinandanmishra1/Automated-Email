import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "allexamsnotifications@gmail.com"
you = "jaihindustanabhi@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    /*
CONFIG STYLES
Please do not delete and edit CSS styles below
*/
/* IMPORTANT THIS STYLES MUST BE ON FINAL EMAIL */
#outlook a {
    padding: 0;
}

.ExternalClass {
    width: 100%;
}

.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {
    line-height: 100%;
}

.es-button {
    mso-style-priority: 100 !important;
    text-decoration: none !important;
}

a[x-apple-data-detectors] {
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
}

.es-desk-hidden {
    display: none;
    float: left;
    overflow: hidden;
    width: 0;
    max-height: 0;
    line-height: 0;
    mso-hide: all;
}

/*
END OF IMPORTANT
*/
s {
    text-decoration: line-through;
}

html,
body {
    width: 100%;
    font-family: 'lucida sans unicode', 'lucida grande', sans-serif;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
}

table {
    mso-table-lspace: 0pt;
    mso-table-rspace: 0pt;
    border-collapse: collapse;
    border-spacing: 0px;
}

table td,
html,
body,
.es-wrapper {
    padding: 0;
    Margin: 0;
}

.es-content,
.es-header,
.es-footer {
    table-layout: fixed !important;
    width: 100%;
}

img {
    display: block;
    border: 0;
    outline: none;
    text-decoration: none;
    -ms-interpolation-mode: bicubic;
}

table tr {
    border-collapse: collapse;
}

p,
hr {
    Margin: 0;
}

h1,
h2,
h3,
h4,
h5 {
    Margin: 0;
    line-height: 120%;
    mso-line-height-rule: exactly;
    font-family: 'lucida sans unicode', 'lucida grande', sans-serif;
}

p,
ul li,
ol li,
a {
    -webkit-text-size-adjust: none;
    -ms-text-size-adjust: none;
    mso-line-height-rule: exactly;
}

.es-left {
    float: left;
}

.es-right {
    float: right;
}

.es-p5 {
    padding: 5px;
}

.es-p5t {
    padding-top: 5px;
}

.es-p5b {
    padding-bottom: 5px;
}

.es-p5l {
    padding-left: 5px;
}

.es-p5r {
    padding-right: 5px;
}

.es-p10 {
    padding: 10px;
}

.es-p10t {
    padding-top: 10px;
}

.es-p10b {
    padding-bottom: 10px;
}

.es-p10l {
    padding-left: 10px;
}

.es-p10r {
    padding-right: 10px;
}

.es-p15 {
    padding: 15px;
}

.es-p15t {
    padding-top: 15px;
}

.es-p15b {
    padding-bottom: 15px;
}

.es-p15l {
    padding-left: 15px;
}

.es-p15r {
    padding-right: 15px;
}

.es-p20 {
    padding: 20px;
}

.es-p20t {
    padding-top: 20px;
}

.es-p20b {
    padding-bottom: 20px;
}

.es-p20l {
    padding-left: 20px;
}

.es-p20r {
    padding-right: 20px;
}

.es-p25 {
    padding: 25px;
}

.es-p25t {
    padding-top: 25px;
}

.es-p25b {
    padding-bottom: 25px;
}

.es-p25l {
    padding-left: 25px;
}

.es-p25r {
    padding-right: 25px;
}

.es-p30 {
    padding: 30px;
}

.es-p30t {
    padding-top: 30px;
}

.es-p30b {
    padding-bottom: 30px;
}

.es-p30l {
    padding-left: 30px;
}

.es-p30r {
    padding-right: 30px;
}

.es-p35 {
    padding: 35px;
}

.es-p35t {
    padding-top: 35px;
}

.es-p35b {
    padding-bottom: 35px;
}

.es-p35l {
    padding-left: 35px;
}

.es-p35r {
    padding-right: 35px;
}

.es-p40 {
    padding: 40px;
}

.es-p40t {
    padding-top: 40px;
}

.es-p40b {
    padding-bottom: 40px;
}

.es-p40l {
    padding-left: 40px;
}

.es-p40r {
    padding-right: 40px;
}

.es-menu td {
    border: 0;
}

.es-menu td a img {
    display: inline-block !important;
}

/*
END CONFIG STYLES
*/
a {
    font-family: 'lucida sans unicode', 'lucida grande', sans-serif;
    font-size: 14px;
    text-decoration: underline;
}

h1 {
    font-size: 30px;
    font-style: normal;
    font-weight: normal;
    color: #333333;
}

h2 {
    font-size: 24px;
    font-style: normal;
    font-weight: normal;
    color: #333333;
}

h3 {
    font-size: 18px;
    font-style: normal;
    font-weight: normal;
    color: #333333;
}

p,
ul li,
ol li {
    font-size: 14px;
    font-family: 'lucida sans unicode', 'lucida grande', sans-serif;
    line-height: 150%;
}

ul li,
ol li {
    Margin-bottom: 15px;
}

.es-menu td a {
    text-decoration: none;
    display: block;
}

.es-wrapper {
    width: 100%;
    height: 100%;
    background-image: ;
    background-repeat: repeat;
    background-position: center top;
}

.es-wrapper-color {
    background-color: #f6f6f6;
}

.es-content-body {
    background-color: #ffffff;
}

.es-content-body p,
.es-content-body ul li,
.es-content-body ol li {
    color: #666666;
}

.es-content-body a {
    color: #128ff3;
}

.es-header {
    background-color: transparent;
    background-image: ;
    background-repeat: repeat;
    background-position: center top;
}

.es-header-body {
    background-color: #ffffff;
}

.es-header-body p,
.es-header-body ul li,
.es-header-body ol li {
    color: #cccccc;
    font-size: 14px;
}

.es-header-body a {
    color: #cccccc;
    font-size: 14px;
}

.es-footer {
    background-color: transparent;
    background-image: ;
    background-repeat: repeat;
    background-position: center top;
}

.es-footer-body {
    background-color: #eaebf0;
}

.es-footer-body p,
.es-footer-body ul li,
.es-footer-body ol li {
    color: #333333;
    font-size: 14px;
}

.es-footer-body a {
    color: #333333;
    font-size: 14px;
}

.es-infoblock,
.es-infoblock p,
.es-infoblock ul li,
.es-infoblock ol li {
    line-height: 120%;
    font-size: 12px;
    color: #cccccc;
}

.es-infoblock a {
    font-size: 12px;
    color: #cccccc;
}

a.es-button {
    border-style: solid;
    border-color: #333333;
    border-width: 10px 20px 10px 20px;
    display: inline-block;
    background: #333333;
    border-radius: 0px;
    font-size: 16px;
    font-family: 'arial', 'helvetica neue', 'helvetica', 'sans-serif';
    font-weight: normal;
    font-style: normal;
    line-height: 120%;
    color: #ffffff;
    text-decoration: none;
    width: auto;
    text-align: center;
}

.es-button-border {
    border-style: solid solid solid solid;
    border-color: #ffffff #ffffff #ffffff #ffffff;
    background: #2cb543;
    border-width: 0px 0px 0px 0px;
    display: inline-block;
    border-radius: 0px;
    width: auto;
}

/*
RESPONSIVE STYLES
Please do not delete and edit CSS styles below.
 
If you don't need responsive layout, please delete this section.
*/
@media only screen and (max-width: 600px) {

    p,
    ul li,
    ol li,
    a {
        font-size: 16px !important;
        line-height: 150% !important;
    }

    h1 {
        font-size: 30px !important;
        text-align: center;
        line-height: 120% !important;
    }

    h2 {
        font-size: 26px !important;
        text-align: center;
        line-height: 120% !important;
    }

    h3 {
        font-size: 20px !important;
        text-align: center;
        line-height: 120% !important;
    }

    h1 a {
        font-size: 30px !important;
    }

    h2 a {
        font-size: 26px !important;
    }

    h3 a {
        font-size: 20px !important;
    }

    .es-menu td a {
        font-size: 16px !important;
    }

    .es-header-body p,
    .es-header-body ul li,
    .es-header-body ol li,
    .es-header-body a {
        font-size: 16px !important;
    }

    .es-footer-body p,
    .es-footer-body ul li,
    .es-footer-body ol li,
    .es-footer-body a {
        font-size: 16px !important;
    }

    .es-infoblock p,
    .es-infoblock ul li,
    .es-infoblock ol li,
    .es-infoblock a {
        font-size: 12px !important;
    }

    *[class="gmail-fix"] {
        display: none !important;
    }

    .es-m-txt-c,
    .es-m-txt-c h1,
    .es-m-txt-c h2,
    .es-m-txt-c h3 {
        text-align: center !important;
    }

    .es-m-txt-r,
    .es-m-txt-r h1,
    .es-m-txt-r h2,
    .es-m-txt-r h3 {
        text-align: right !important;
    }

    .es-m-txt-l,
    .es-m-txt-l h1,
    .es-m-txt-l h2,
    .es-m-txt-l h3 {
        text-align: left !important;
    }

    .es-m-txt-r img,
    .es-m-txt-c img,
    .es-m-txt-l img {
        display: inline !important;
    }

    .es-button-border {
        display: block !important;
    }

    a.es-button {
        font-size: 20px !important;
        display: block !important;
        border-width: 10px 20px 10px 20px !important;
    }

    .es-btn-fw {
        border-width: 10px 0px !important;
        text-align: center !important;
    }

    .es-adaptive table,
    .es-btn-fw,
    .es-btn-fw-brdr,
    .es-left,
    .es-right {
        width: 100% !important;
    }

    .es-content table,
    .es-header table,
    .es-footer table,
    .es-content,
    .es-footer,
    .es-header {
        width: 100% !important;
        max-width: 600px !important;
    }

    .es-adapt-td {
        display: block !important;
        width: 100% !important;
    }

    .adapt-img {
        width: 100% !important;
        height: auto !important;
    }

    .es-m-p0 {
        padding: 0px !important;
    }

    .es-m-p0r {
        padding-right: 0px !important;
    }

    .es-m-p0l {
        padding-left: 0px !important;
    }

    .es-m-p0t {
        padding-top: 0px !important;
    }

    .es-m-p0b {
        padding-bottom: 0 !important;
    }

    .es-m-p20b {
        padding-bottom: 20px !important;
    }

    .es-mobile-hidden,
    .es-hidden {
        display: none !important;
    }

    tr.es-desk-hidden,
    td.es-desk-hidden,
    table.es-desk-hidden {
        display: table-row !important;
        width: auto !important;
        overflow: visible !important;
        float: none !important;
        max-height: inherit !important;
        line-height: inherit !important;
    }

    .es-desk-menu-hidden {
        display: table-cell !important;
    }

    table.es-table-not-adapt,
    .esd-block-html table {
        width: auto !important;
    }

    table.es-social {
        display: inline-block !important;
    }

    table.es-social td {
        display: inline-block !important;
    }
}

/*
END RESPONSIVE STYLES
*/
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
    <!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#f6f6f6"></v:fill>
			</v:background>
		<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table cellpadding="0" cellspacing="0" class="es-content esd-header-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="es-adaptive esd-stripe" esd-custom-block-id="2815" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p10" esd-general-paddings-checked="false" align="left">
                                                        <!--[if mso]><table width="580" cellpadding="0" cellspacing="0"><tr><td width="280" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="280" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="es-infoblock esd-block-text" align="left"><span style="font-family:tahoma,verdana,segoe,sans-serif;"><span style="text-align: center;">Put your preheader text here</span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="280" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="280" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="right" class="es-infoblock esd-block-text">
                                                                                        <p><a href="https://viewstripo.email/" target="_blank" class="view">View in browser</a></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-header" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2816" align="center">
                                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p10" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="580" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="center" style="font-size:0"><a href="https://viewstripo.email/" target="_blank"><img src="https://tlr.stripocdn.email/content/guids/CABINET_a2176b7189cddc87b3b9c3862abf6a44/images/39891506951989324.png" alt="Electros logo" title="Electros logo" width="159"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" style="background-color: #333333;" esd-custom-block-id="2817" bgcolor="#333333" align="center">
                                        <table class="es-content-body" style="background-color: #333333;" width="600" cellspacing="0" cellpadding="0" bgcolor="#333333" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p5t es-p5b" style="background-color: #333333;" esd-general-paddings-checked="false" bgcolor="#333333" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="600" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-menu" esd-img-prev-h="16" esd-img-prev-w="16">
                                                                                        <table class="es-menu" width="100%" cellspacing="0" cellpadding="0">
                                                                                            <tbody>
                                                                                                <tr class="links">
                                                                                                    <td class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px; padding-top: 10px; " width="20.00%" bgcolor="transparent" align="center"><a style="color: #ffffff;" href="https://viewstripo.email/">Catalog</a></td>
                                                                                                    <td class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px; padding-top: 10px; " width="20.00%" bgcolor="transparent" align="center"><a style="color: #ffffff;" href="https://viewstripo.email/">New arrivals</a></td>
                                                                                                    <td class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px; padding-top: 10px; " width="20.00%" bgcolor="transparent" align="center"><a style="color: #ffffff;" href="https://viewstripo.email/">Sale</a></td>
                                                                                                    <td class="es-p10t es-p10b es-p5r es-p5l es-hidden" style="padding-bottom: 10px; padding-top: 10px; " width="20.00%" bgcolor="transparent" align="center"><a style="color: #ffffff;" href="https://viewstripo.email/">Blog</a></td>
                                                                                                    <td class="es-p10t es-p10b es-p5r es-p5l es-hidden" style="padding-bottom: 10px; padding-top: 10px; " width="20.00%" bgcolor="transparent" align="center"><a style="color: #ffffff;" href="https://viewstripo.email/">Contacts</a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr></tr>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2814" align="center">
                                        <table class="es-content-body" style="background-color: #eaebf0;" width="600" cellspacing="0" cellpadding="0" bgcolor="#eaebf0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="600" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-banner" style="position: relative;" align="center" esdev-config="h13"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img esdev-stretch-width esdev-banner-rendered" src="https://tlr.stripocdn.email/content/guids/bannerImgGuid/images/62921577373890673.png" alt="Back to school sale. 45% Off Storewide. Use code: B2SCHOOL ends 8/17" title="Back to school sale. 45% Off Storewide. Use code: B2SCHOOL ends 8/17" width="100%" style="display: block;"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr></tr>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2787" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t" esd-custom-block-id="14920" align="left">
                                                        <!--[if mso]><table width="600" cellpadding="0" 
                        cellspacing="0"><tr><td width="290" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="290" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/16351533131084157.jpg" alt="Laptops & PCs" style="display: block;" title="Laptops & PCs" width="290"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20t es-p20b" bgcolor="#eaebf0" align="center"><span class="es-button-border" style="border-width: 0px; border-style: solid; border-color: transparent; background: #eaebf0 none repeat scroll 0% 0%;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="border-width: 0px; font-weight: normal; color: #666666; font-family: 'lucida sans unicode', 'lucida grande', sans-serif; background: #eaebf0 none repeat scroll 0% 0%; border-color: #eaebf0;">Laptops & PCs</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="290" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="290" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/74071533132114776.jpg" alt="Smartphones" style="display: block;" title="Smartphones" width="290"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20t es-p20b" bgcolor="#eaebf0" align="center"><span class="es-button-border" style="border-width: 0px; border-style: solid; border-color: transparent; background: #eaebf0 none repeat scroll 0% 0%;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="border-width: 0px; font-weight: normal; color: #666666; font-family: 'lucida sans unicode', 'lucida grande', sans-serif; background: #eaebf0 none repeat scroll 0% 0%; border-color: #eaebf0;">Smartphones</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p20b" align="left">
                                                        <!--[if mso]><table width="600" cellpadding="0" 
                        cellspacing="0"><tr><td width="290" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="290" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/78851533131723011.jpg" alt="Audio & Instruments" style="display: block;" title="Audio & Instruments" width="290"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20t es-p20b" bgcolor="#eaebf0" align="center"><span class="es-button-border" style="border-width: 0px; border-style: solid; border-color: transparent; background: #eaebf0 none repeat scroll 0% 0%;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="border-width: 0px; font-weight: normal; color: #666666; font-family: 'lucida sans unicode', 'lucida grande', sans-serif; background: #eaebf0 none repeat scroll 0% 0%; border-color: #eaebf0;">Audio & Instruments</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="290" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="290" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/84721533131809421.jpg" alt="Household appliances" style="display: block;" title="Household appliances" width="290"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20t es-p20b" bgcolor="#eaebf0" align="center"><span class="es-button-border" style="border-width: 0px; border-style: solid; border-color: transparent; background: #eaebf0 none repeat scroll 0% 0%;"><a href="https://viewstripo.email/" class="es-button" target="_blank" style="border-width: 0px; font-weight: normal; color: #666666; font-family: 'lucida sans unicode', 'lucida grande', sans-serif; background: #eaebf0 none repeat scroll 0% 0%; border-color: #eaebf0;">Household appliances</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr></tr>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2843" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p15t es-p5b es-p20r es-p20l" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text" align="center">
                                                                                        <h2>Selected just for you<br></h2>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p20b es-p20r es-p20l" esd-custom-block-id="14919" align="left">
                                                        <!--[if mso]><table width="560" cellpadding="0" 
                            cellspacing="0"><tr><td width="194" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="174" align="center" esdev-config="h9">
                                                                        <table style="background-color: #eaebf0;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#eaebf0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p15t es-p15r es-p15l" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/35251533195252889.png" alt="Essential PH-1 4GB + 128GB" style="display: block;" title="Essential PH-1 4GB + 128GB" height="150"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td esd-links-color="#333333" class="esd-block-text es-p20t es-p5b es-p10r es-p10l" align="center">
                                                                                        <p style="color: #333333; font-size: 16px;" class="product-name">Essential PH-1 4GB + 128GB</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t es-p20b" align="center">
                                                                                        <h4 style="color: #333333;" class="price">$190.80</h4>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20b es-p10r es-p10l" align="center"><span class="es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">Shop now</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td class="es-hidden" width="20"></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="173" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="173" align="center" esdev-config="h10">
                                                                        <table style="background-color: #eaebf0;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#eaebf0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p15t es-p15r es-p15l" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/52061533194804257.png" alt="Sony MDR100 Headphones" style="display: block;" title="Sony MDR100 Headphones" height="148"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td esd-links-color="#333333" class="esd-block-text es-p20t es-p5b es-p10r es-p10l" align="center">
                                                                                        <p style="color: #333333; font-size: 16px;" class="product-name">Sony MDR100 Headphones</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t es-p20b" align="center">
                                                                                        <h4 style="color: #333333;" class="price">$220.00</h4>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20b es-p10r es-p10l" align="center"><span class="es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">Shop now</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="173" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="173" align="center" esdev-config="h11">
                                                                        <table style="background-color: #eaebf0;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#eaebf0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p15t es-p15r es-p15l" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_903af91e9fe35af23d044f3ee3ae3f76/images/58981533194541693.png" alt="Apple Watch Series 3 Aluminum" style="display: block;" title="Apple Watch Series 3 Aluminum" height="148"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td esd-links-color="#333333" class="esd-block-text es-p20t es-p5b es-p10r es-p10l" align="center">
                                                                                        <p style="color: #333333; font-size: 16px;" class="product-name">Apple Watch Series 3 Aluminum</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t es-p20b" align="center">
                                                                                        <h4 style="color: #333333;" class="price">$350.55</h4>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p20b es-p10r es-p10l" align="center"><span class="es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">Shop now</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2836" align="center">
                                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="left" style="font-size:0"><a target="_blank" href="https://viewstripo.email/"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_a2176b7189cddc87b3b9c3862abf6a44/images/39891506951989324.png" alt="Electros logo" title="Electros logo" width="148"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p5b es-p20r es-p20l" esd-general-paddings-checked="false" align="left">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="194"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="174" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c" align="left">
                                                                                        <p><span style="font-family: helvetica, 'helvetica neue', arial, verdana, sans-serif; line-height: 150%;">108 Karna Street</span></p>
                                                                                        <p><span style="font-family: helvetica,helvetica neue,arial,verdana,sans-serif; line-height: 150%;">San Francisco, CA 34545</span></p>
                                                                                        <p><br></p>
                                                                                        <p><span style="font-family: helvetica,helvetica neue,arial,verdana,sans-serif; line-height: 150%;">(251) 123-4567</span></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td class="es-hidden" width="20"></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="173"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="173" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c" esdev-links-color="#333333" align="left">
                                                                                        <p><a target="_blank" style="line-height: 150%; font-family: 'lucida sans unicode','lucida grande','sans-serif';" href="https://viewstripo.email/">Laptops</a></p>
                                                                                        <p><a target="_blank" href="https://viewstripo.email/">Household appliances</a></p>
                                                                                        <p><a target="_blank" href="https://viewstripo.email/">Camera</a></p>
                                                                                        <p><a target="_blank" href="https://viewstripo.email/">Mobile</a></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="173"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="173" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c" align="left">
                                                                                        <p><a href="https://viewstripo.email/" target="_blank">Delivery</a></p>
                                                                                        <p><a href="https://viewstripo.email/" target="_blank">Returns</a></p>
                                                                                        <p><a href="https://viewstripo.email/" target="_blank">Blog</a></p>
                                                                                        <p><a href="https://viewstripo.email/" target="_blank">FAQ</a></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p20b es-p20r es-p20l" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-social es-p10b" align="center" style="font-size:0">
                                                                                        <table class="es-table-not-adapt es-social" cellspacing="0" cellpadding="0">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td class="es-p10r" valign="top" align="center"><a target="_blank" href><img title="Twitter" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/twitter-circle-black.png" alt="Tw" width="32"></a></td>
                                                                                                    <td class="es-p10r" valign="top" align="center"><a target="_blank" href><img title="Facebook" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/facebook-circle-black.png" alt="Fb" width="32"></a></td>
                                                                                                    <td class="es-p10r" valign="top" align="center"><a target="_blank" href><img title="Youtube" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/youtube-circle-black.png" alt="Yt" width="32"></a></td>
                                                                                                    <td valign="top" align="center"><a target="_blank" href><img title="Instagram" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/instagram-circle-black.png" alt="Ig" width="32"></a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td esdev-links-color="#333333" align="center" class="esd-block-text es-p5t">
                                                                                        <p style="line-height: 200%; font-size: 13px;"><a target="_blank" style="line-height: 150%; font-size: 13px;" class="view" href="https://viewstripo.email/">View in Browser</a> | <a target="_blank" style="line-height: 150%; font-size: 13px;" href="https://viewstripo.email/">Update Preferences</a> | <a target="_blank" style="line-height: 150%; font-size: 13px;" class="unsubscribe">Unsubscribe</a></p>
                                                                                        <p style="line-height: 200%;">Vector graphics designed by <a target="_blank" href="https://www.freepik.com/">Freepik</a>.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="esd-footer-popover es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" style="background-color: transparent;" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-infoblock made_with" align="center" style="font-size:0"><a target="_blank" href="https://viewstripo.email/?utm_source=templates&utm_medium=email&utm_campaign=gadgets_2&utm_content=back_to_school"><img src="https://tlr.stripocdn.email/content/guids/cab_pub_7cbbc409ec990f19c78c75bd1e06f215/images/78411525331495932.png" alt style="display: block;" height="56"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.gmail.com:587')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.ehlo()
passw=input("Enter Password")
s.starttls()

s.login(me, passw)

s.sendmail(me, you, msg.as_string())
s.quit()
print("Success")