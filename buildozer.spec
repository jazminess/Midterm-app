[app]
android.p4a_whitelist = hostpython3==3.11.9,python3==3.11.9
title = Easy Physics
package.name = easyphysics
package.domain = org.jazminess

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

android.accept_sdk_license = True

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
