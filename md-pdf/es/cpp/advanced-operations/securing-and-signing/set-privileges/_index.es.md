---
title: Establecer Privilegios, Encriptar y Desencriptar Archivo PDF usando C++
linktitle: Encriptar y Desencriptar Archivo PDF
type: docs
weight: 20
url: /cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: encriptar pdf,proteger pdf con contraseña,desencriptar pdf,c++
description: Encriptar Archivo PDF con C++ usando Diferentes Tipos de Encriptación y Algoritmos. También, desencriptar Archivos PDF usando Contraseña de Propietario.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Establecer Privilegios en un Archivo PDF Existente

Para establecer privilegios en un archivo PDF existente Aspose.PDF para C++ usa la clase [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) y especifica los derechos que deseas aplicar al documento. Una vez que los privilegios han sido definidos, pasa este objeto como un argumento al método [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

El siguiente fragmento de código te muestra cómo establecer los privilegios de un archivo PDF.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cargar un archivo PDF de origen
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instanciar objeto de privilegios de documento

    // Aplicar restricciones a todos los privilegios
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Solo permitir lectura de pantalla
    documentPrivilege->set_AllowScreenReaders(true);

    // Encriptar el archivo con contraseña de Usuario y Propietario.
    // Necesita establecer la contraseña, para que una vez que el usuario vea el archivo con la contraseña de usuario,

    // Solo la opción de lectura de pantalla está habilitada
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // Guardar documento actualizado
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Encriptar archivo PDF utilizando diferentes tipos de encriptación y algoritmos

Para encriptar el archivo PDF use el método [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) para encriptar un archivo PDF.

El siguiente fragmento de código te muestra cómo cifrar archivos PDF.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // Cadena para el nombre del camino.
    String _dataDir("C:\\Samples\\");

    // Cargar un archivo PDF de origen
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instanciar objeto de Privilegios del Documento
    // Aplicar restricciones en todos los privilegios
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Solo permitir lectura de pantalla
    documentPrivilege->set_AllowScreenReaders(true);
    // Cifrar el archivo con contraseña de Usuario y Propietario.
    // Necesita establecer la contraseña, para que una vez que el usuario vea el archivo con la
    // contraseña de usuario,
    // Solo la opción de lectura de pantalla está habilitada
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // Guardar el documento actualizado
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Desencriptar archivo PDF usando contraseña de propietario

Para desencriptar el archivo PDF, primero necesitas crear un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) y abrir el PDF usando la contraseña del propietario. Después de eso, necesitas llamar al método [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a).

```cpp
void SecuringAndSigning::DecryptPDFFile() {


// Cadena para el nombre de la ruta.

String _dataDir("C:\\Samples\\");


// Abrir documento

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// Desencriptar PDF

document->Decrypt();


// Guardar PDF actualizado

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## Cambiar la Contraseña de un Archivo PDF

Dado que tus PDFs pueden contener información importante y confidencial, deben permanecer seguros. En consecuencia, es posible que necesites cambiar la contraseña de tu documento PDF.

Si deseas cambiar la contraseña de un archivo PDF, primero necesitas abrir el archivo PDF usando la contraseña de propietario con el objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Después de eso, necesitas llamar al método [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d).

El siguiente fragmento de código te muestra cómo cambiar la contraseña de un archivo PDF.
```cpp
void SecuringAndSigning::ChangePassword_PDF_File() {

// String for path name.

String _dataDir("C:\\Samples\\");


// Open document

auto document = MakeObject<Document>(_dataDir + u"ChangePassword.pdf", u"owner");

// Change password

document->ChangePasswords(u"owner", u"newuser", u"newowner");

// Save updated PDF

document->Save(_dataDir + u"ChangePassword_out.pdf");
}
```

## Cómo - determinar si el PDF de origen está protegido con contraseña

Un documento PDF cifrado con la contraseña del usuario no se puede abrir sin una contraseña.
``` Debemos determinar si el documento está protegido con contraseña antes de intentar abrirlo. A veces hay documentos que no requieren información de contraseña al abrirlos, pero requieren información para editar el contenido del archivo. Así que para cumplir con los requisitos anteriores, la clase [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) presente en Aspose.PDF.Facades proporciona las propiedades que pueden ayudar a determinar la información requerida.

### Obtener información sobre la seguridad del documento PDF

PdfFileInfo contiene tres propiedades para obtener información sobre la seguridad del documento PDF.

1. La propiedad PasswordType devuelve un valor de enumeración PasswordType:
    - PasswordType.None - el documento no está protegido con contraseña
    - PasswordType.User - el documento se abrió con una contraseña de usuario (o documento abierto)
    - PasswordType.Owner - el documento se abrió con una contraseña de propietario (o permisos, editar)

    - PasswordType.Inaccessible - el documento está protegido con contraseña pero se necesita la contraseña para abrirlo mientras se proporcionó una contraseña inválida (o ninguna contraseña).2. propiedad booleana HasOpenPassword - se utiliza para determinar si el archivo de entrada requiere una contraseña al abrirlo.  
3. propiedad booleana HasEditPassword - se utiliza para determinar si el archivo de entrada requiere una contraseña para editar su contenido.

### Determinar la contraseña correcta de un Array

A veces hay un requisito para determinar la contraseña correcta de un array de contraseñas y abrir el documento con la contraseña correcta. El siguiente fragmento de código demuestra los pasos para iterar a través del array de contraseñas e intentar abrir el documento con la contraseña correcta.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// Cadena para el nombre de la ruta.

String _dataDir("C:\\Samples\\");


// Cargar archivo PDF de origen

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// Determinar si el PDF de origen está encriptado

Console::WriteLine(u"El archivo está protegido con contraseña {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"El número de páginas en el documento es = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"La contraseña = {0} no es correcta", passwords[passwordcount]);


}

}

Console::WriteLine(u"Prueba finalizada");
}
```