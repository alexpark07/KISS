### Dynamic Analysis with NetBeans

#### Make a file with debuggable option

``java -jar apktool.jar d apk_file_name.apk out``

``java -jar apktool.jar b out apk_file_name_debuggable.apk``

#### Code Signing

``java -jar signapk.jar testkey.x509.pem testkey.pk8 apk_file_name_debuggable.apk apk_file_name_signed.apk``

#### Run NetBeans for Dynamic Analysis

1. Java Project with Existing Sources.

2. Select ``out`` directory without ``dist`` directory to avoid error(s)

3. Add JAR/Folder to add ``android.jar`` in SDK

4. Debug > Attach Debugger... > JPDA (Java Debugger) then it'll be connected the target APP

5. Set new breakpoint (breakpoint type: ``Line``)
