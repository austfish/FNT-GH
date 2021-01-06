info_modes = {'login': 'inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth',
              'signup': 'inurl:signup | inurl:register | intitle:Signup',
              'phpinfo': 'ext:php intitle:phpinfo "published by the PHP Group"'}
for info in info_modes:
    print(info_modes[info])