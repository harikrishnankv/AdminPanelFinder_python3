import requests,webbrowser

statusCodeSet = {100, 200, 201, 207, 302, 500}

def checkSubdomain(url):
    if url[:4] == "http":
        protocol = 0
        if url[4] == "s":
            protocol = 1
            if url[8:12]=="www.":
                urlSplit= url[12:]
            else:
                urlSplit=url[8:]
        else:
            if url[7:11]=="www.":
                 urlSplit= url[11:]
            else:
               urlSplit = url[7:]
    #print(urlSplit)
    subDomainList=["admin.","panel.","login.","Admin.","Panel.","Login."]
    status = 0
    for subDomain in subDomainList:
        if protocol:
            testUrl="https://"+subDomain+urlSplit
        else:
            testUrl = "http://" + subDomain+ urlSplit
        print(testUrl)
        try:
            statusValue=requests.post(testUrl)
            status=statusValue.status_code
            print(testUrl, end="   ")
            print(status)
            if status in statusCodeSet:
                return status, testUrl

        except:
            print(f"\033[1;37;40m {testUrl}    ..trying")
    print("\033[1;31;40m    Sorry we Give Up :/ ")
    exit(0)

def checkUrl(siteURL):
    #adminQuery = ['admin/', 'admin', 'Login/Admin','Admin', 'admin.php', 'administrator/', 'administrator', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 'usuario/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'usuarios', 'usuario', 'moderator', 'webadmin', 'adminarea', 'bb-admin', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm', 'adminLogin', 'admin_area', 'panel-administracion', 'instadmin', 'memberadmin', 'administratorlogin', 'adm/', 'admin/account.php', 'admin/index.php', 'admin/login.php', 'admin/admin.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php', 'admin/home.php', 'admin_area/login.html', 'admin_area/index.html', 'admin/controlpanel.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php', 'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php', 'administrator/account.php', 'administrator.php', 'admin_area/admin.html', 'pages/admin/admin-login.php', 'admin/admin-login.php', 'admin-login.php', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html', 'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php', 'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html', 'controlpanel.php', 'admincontrol.php', 'admin/adminLogin.html', 'adminLogin.html', 'home.html', 'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php', 'account.html', 'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php', 'adminarea/index.php', 'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php', 'panel-administracion/admin.php', 'modelsearch/index.php', 'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php', 'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php', 'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php', 'account.asp', 'admin/account.asp', 'admin/index.asp', 'admin/login.asp', 'admin/admin.asp', 'admin_area/admin.asp', 'admin_area/login.asp', 'admin_area/index.asp', 'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp', 'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp', 'admin/admin-login.asp', 'admin-login.asp', 'admin/cp.asp', 'cp.asp', 'administrator/account.asp', 'administrator.asp', 'acceso.asp', 'login.asp', 'modelsearch/login.asp', 'moderator.asp', 'moderator/login.asp', 'administrator/login.asp', 'moderator/admin.asp', 'controlpanel.asp', 'user.asp', 'admincontrol.asp', 'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp', 'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp', 'admin_login.asp', 'panel-administracion/login.asp', 'adminLogin.asp', 'admin/adminLogin.asp', 'home.asp', 'adminarea/index.asp', 'adminarea/admin.asp', 'adminarea/login.asp', 'panel-administracion/index.asp', 'panel-administracion/admin.asp', 'modelsearch/index.asp', 'modelsearch/admin.asp', 'administrator/index.asp', 'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp', 'admin2/index.asp', 'adm/index.asp', 'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp', 'siteadmin/login.asp', 'siteadmin/index.asp', 'admin/account.cfm', 'admin/index.cfm', 'admin/login.cfm', 'admin/admin.cfm', 'admin_area/admin.cfm', 'admin_area/login.cfm', 'siteadmin/login.cfm', 'siteadmin/index.cfm', 'admin_area/index.cfm', 'bb-admin/index.cfm', 'bb-admin/login.cfm', 'bb-admin/admin.cfm', 'admin/home.cfm', 'admin/controlpanel.cfm', 'admin.cfm', 'admin/cp.cfm', 'cp.cfm', 'administrator/index.cfm', 'administrator/login.cfm', 'nsw/admin/login.cfm', 'webadmin/login.cfm', 'admin/admin_login.cfm', 'admin_login.cfm', 'administrator/account.cfm', 'administrator.cfm', 'pages/admin/admin-login.cfm', 'admin/admin-login.cfm', 'admin-login.cfm', 'login.cfm', 'modelsearch/login.cfm', 'moderator.cfm', 'moderator/login.cfm', 'moderator/admin.cfm', 'account.cfm', 'controlpanel.cfm', 'admincontrol.cfm', 'acceso.cfm', 'rcjakar/admin/login.cfm', 'webadmin.cfm', 'webadmin/index.cfm', 'webadmin/admin.cfm', 'adminpanel.cfm', 'user.cfm', 'panel-administracion/login.cfm', 'wp-login.cfm', 'adminLogin.cfm', 'admin/adminLogin.cfm', 'home.cfm', 'adminarea/index.cfm', 'adminarea/admin.cfm', 'adminarea/login.cfm', 'panel-administracion/index.cfm', 'panel-administracion/admin.cfm', 'modelsearch/index.cfm', 'modelsearch/admin.cfm', 'admincontrol/login.cfm', 'adm/admloginuser.cfm', 'admloginuser.cfm', 'admin2.cfm', 'admin2/login.cfm', 'admin2/index.cfm', 'usuarios/login.cfm', 'adm/index.cfm', 'adm.cfm', 'affiliate.cfm', 'adm_auth.cfm', 'memberadmin.cfm', 'administratorlogin.cfm', 'admin/account.js', 'admin/index.js', 'admin/login.js', 'admin/admin.js', 'admin_area/admin.js', 'admin_area/login.js', 'siteadmin/login.js', 'siteadmin/index.js', 'admin_area/index.js', 'bb-admin/index.js', 'bb-admin/login.js', 'bb-admin/admin.js', 'admin/home.js', 'admin/controlpanel.js', 'admin.js', 'admin/cp.js', 'cp.js', 'administrator/index.js', 'administrator/login.js', 'nsw/admin/login.js', 'webadmin/login.js', 'admin/admin_login.js', 'admin_login.js', 'administrator/account.js', 'administrator.js', 'pages/admin/admin-login.js', 'admin/admin-login.js', 'admin-login.js', 'login.js', 'modelsearch/login.js', 'moderator.js', 'moderator/login.js', 'moderator/admin.js', 'account.js', 'controlpanel.js', 'admincontrol.js', 'rcjakar/admin/login.js', 'webadmin.js', 'webadmin/index.js', 'acceso.js', 'webadmin/admin.js', 'adminpanel.js', 'user.js', 'panel-administracion/login.js', 'wp-login.js', 'adminLogin.js', 'admin/adminLogin.js', 'home.js', 'adminarea/index.js', 'adminarea/admin.js', 'adminarea/login.js', 'panel-administracion/index.js', 'panel-administracion/admin.js', 'modelsearch/index.js', 'modelsearch/admin.js', 'admincontrol/login.js', 'adm/admloginuser.js', 'admloginuser.js', 'admin2.js', 'admin2/login.js', 'admin2/index.js', 'usuarios/login.js', 'adm/index.js', 'adm.js', 'affiliate.js', 'adm_auth.js', 'memberadmin.js', 'administratorlogin.js', 'admin/account.cgi', 'admin/index.cgi', 'admin/login.cgi', 'admin/admin.cgi', 'admin_area/admin.cgi', 'admin_area/login.cgi', 'siteadmin/login.cgi', 'siteadmin/index.cgi', 'admin_area/index.cgi', 'bb-admin/index.cgi', 'bb-admin/login.cgi', 'bb-admin/admin.cgi', 'admin/home.cgi', 'admin/controlpanel.cgi', 'admin.cgi', 'admin/cp.cgi', 'cp.cgi', 'administrator/index.cgi', 'administrator/login.cgi', 'nsw/admin/login.cgi', 'webadmin/login.cgi', 'admin/admin_login.cgi', 'admin_login.cgi', 'administrator/account.cgi', 'administrator.cgi', 'pages/admin/admin-login.cgi', 'admin/admin-login.cgi', 'admin-login.cgi', 'login.cgi', 'modelsearch/login.cgi', 'moderator.cgi', 'moderator/login.cgi', 'moderator/admin.cgi', 'account.cgi', 'controlpanel.cgi', 'admincontrol.cgi', 'rcjakar/admin/login.cgi', 'webadmin.cgi', 'webadmin/index.cgi', 'acceso.cgi', 'webadmin/admin.cgi', 'adminpanel.cgi', 'user.cgi', 'panel-administracion/login.cgi', 'wp-login.cgi', 'adminLogin.cgi', 'admin/adminLogin.cgi', 'home.cgi', 'adminarea/index.cgi', 'adminarea/admin.cgi', 'adminarea/login.cgi', 'panel-administracion/index.cgi', 'panel-administracion/admin.cgi', 'modelsearch/index.cgi', 'modelsearch/admin.cgi', 'admincontrol/login.cgi', 'adm/admloginuser.cgi', 'admloginuser.cgi', 'admin2.cgi', 'admin2/login.cgi', 'admin2/index.cgi', 'usuarios/login.cgi', 'adm/index.cgi', 'adm.cgi', 'affiliate.cgi', 'adm_auth.cgi', 'memberadmin.cgi', 'administratorlogin.cgi', 'admin_panel/', 'admin_panel', 'admin_panel.html', 'adm_cp/', 'adm_cp']
    adminQuery = open("adminPanel.txt", "r")
    status = 0
    print(siteURL)
    for line in adminQuery:
        testUrl = siteURL + "/" + line.strip()
        statusValue = requests.post(testUrl)
        status = statusValue.status_code
        print(testUrl)
            #print(status)
        if status in statusCodeSet:
            adminQuery.close()
            return status,testUrl
    adminQuery.close()
    print("\033[0;31;40m   Sorry we Give Up :/ ")
    exit(0)

def getWebsiteAddress():
    return input("[++] Enter the URL(example: https://www.xyz.com) [++] :  ").strip()

def printResult(statusValue,testUrl):

    if statusValue in statusCodeSet:
        print(f" Hey we found something...!!!   try this url-->  {testUrl}")
        print("Trying to open it in your browser...")
        webbrowser.open(testUrl)

if __name__ == '__main__':
    url = getWebsiteAddress()
    select = int(input("[+ +]  Scan Admin Panel by checking sub Domain (Enter 1) or by Normal Scan (Enter 2 ) [++]    : ").strip())
    if select==1:
        status,finalUrl=checkSubdomain(url)
        printResult(status, finalUrl)
    elif select==2:
        status,finalUrl=checkUrl(url)
        printResult(status,finalUrl)

