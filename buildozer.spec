[app]
title = Manou Assistant
version = 0.1
package.name = manouapp
package.domain = org.manou
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
requirements = python3,kivy,git,urllib3,certifi,idna,charset-normalizer,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
root = 1

