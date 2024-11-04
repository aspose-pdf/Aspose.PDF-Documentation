---
title: Establecer Privilegios, Cifrar y Descifrar Archivo PDF 
linktitle: Cifrar y Descifrar Archivo PDF
type: docs
weight: 20
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: cifrar pdf,proteger con contraseña pdf,descifrar pdf,java
description: Cifrar archivo PDF con Java utilizando diferentes tipos de cifrado y algoritmos. También, descifrar archivos PDF usando la contraseña del propietario.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Establecer Privilegios en un Archivo PDF Existente

Para establecer privilegios en un archivo PDF, crea un objeto de la clase DocumentPrivilege y especifica los derechos que deseas aplicar al documento.
 Una vez que se han definido los privilegios, pase este objeto como un argumento al método [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). El siguiente fragmento de código le muestra cómo establecer los privilegios de un archivo PDF.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // Cargar un archivo PDF de origen
   Document document = new Document(_dataDir + "input.pdf");

   // Instanciar el objeto de Privilegios de Documento
   // Aplicar restricciones a todos los privilegios
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Solo permitir la lectura de pantalla
   documentPrivilege.setAllowScreenReaders(true);
   // Encriptar el archivo con contraseña de Usuario y Propietario.
   // Necesita establecer la contraseña, para que una vez que el usuario vea el archivo con la contraseña de usuario,
   // Solo la opción de lectura de pantalla esté habilitada
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Guardar el documento actualizado
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Encriptar archivo PDF usando diferentes tipos de cifrado y algoritmos

Puede utilizar el método [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para encriptar un archivo PDF. Puede pasar la contraseña de usuario, la contraseña de propietario y los permisos al método [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-). Además de eso, puede pasar cualquier valor del enum [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm). Este enum proporciona diferentes combinaciones de algoritmos de cifrado y tamaños de clave. Puede pasar el valor de su elección. Finalmente, guarde el archivo PDF encriptado usando el método [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

>Por favor, especifique diferentes contraseñas de usuario y propietario al encriptar el archivo PDF.

El siguiente fragmento de código te muestra cómo cifrar archivos PDF.

```java
public static void EncryptPDFFile() {
   // Cargar un archivo PDF de origen
   Document document = new Document(_dataDir + "input.pdf");

   // Instanciar objeto de Privilegios del Documento
   // Aplicar restricciones en todos los privilegios
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Solo permitir lectura de pantalla
   documentPrivilege.setAllowScreenReaders(true);
   // Cifrar el archivo con contraseña de Usuario y Propietario.
   // Necesita establecer la contraseña, para que una vez que el usuario vea el archivo con la
   // contraseña de usuario,
   // Solo la opción de lectura de pantalla esté habilitada
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Guardar documento actualizado
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Desencriptar archivo PDF usando la contraseña del propietario

Para desencriptar el archivo PDF, primero necesitas crear un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y abrir el PDF usando la contraseña del propietario.
 Después de eso, necesitas llamar al método [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Finalmente, guarda el archivo PDF actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). El siguiente fragmento de código te muestra cómo descifrar el archivo PDF.

```java
public static void DecryptPDFFile() {
   // Abrir documento
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // Descifrar PDF
   document.decrypt();

   // Guardar PDF actualizado
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## Cambiar la Contraseña de un Archivo PDF

Si deseas cambiar la contraseña de un archivo PDF, primero necesitas abrir el archivo PDF usando la contraseña del propietario con el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Después de eso, necesitas llamar al método [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Necesitas pasar la contraseña actual del propietario junto con la nueva contraseña de usuario y la nueva contraseña de propietario a este método. Finalmente, guarda el archivo PDF actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código te muestra cómo cambiar la contraseña de un archivo PDF.

```java
public static void ChangePassword_PDF_File() {
   // Abrir documento
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // Cambiar contraseña
   document.changePasswords("owner", "newuser", "newowner");
   // Guardar PDF actualizado
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## Cómo - determinar si el PDF de origen está protegido con contraseña

Aspose.PDF para Java proporciona grandes capacidades para tratar con documentos PDF. Cuando se utiliza la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) del paquete com.aspose.pdf para abrir un documento PDF que está protegido con contraseña, necesitamos proporcionar la información de la contraseña como un argumento para el constructor de Document y en caso de que esta información no se proporcione, se genera un mensaje de error. De hecho, al intentar abrir un archivo PDF con el objeto Document, el constructor intenta leer el contenido del archivo PDF y en caso de que no se proporcione la contraseña correcta, se genera un mensaje de error (esto ocurre para prevenir el acceso no autorizado al documento).

Al tratar con archivos PDF cifrados, puede encontrarse con el escenario en el que estaría interesado en detectar si un PDF tiene una contraseña de apertura y/o una contraseña de edición. A veces hay documentos que no requieren información de contraseña al abrirlos, pero requieren información para editar el contenido del archivo. Así que, para cumplir con los requisitos anteriores, la clase PdfFileInfo presente en el paquete com.aspose.pdf.facades proporciona los métodos que pueden ayudar a determinar la información requerida.

### Obtener información sobre la seguridad del documento PDF

PdfFileInfo contiene tres métodos para obtener información sobre la seguridad del documento PDF.

1. El método getPasswordType() devuelve un valor de enumeración PasswordType:
    1. PasswordType.None - el documento no está protegido con contraseña
    1. PasswordType.User - el documento fue abierto con la contraseña de usuario (o de apertura del documento)
    1. PasswordType.Owner - el documento fue abierto con la contraseña de propietario (o de permisos, edición)
    1. PasswordType.Inaccessible - el documento está protegido con contraseña pero se necesita una contraseña para abrirlo mientras que se suministró una contraseña inválida (o no se proporcionó contraseña).
1. El método hasOpenPassword() se utiliza para determinar si el archivo de entrada requiere una contraseña al abrirlo.
1. El método hasEditPassword() se utiliza para determinar si el archivo de entrada requiere una contraseña para editar su contenido.

### Determinar la contraseña correcta de un Array

A veces hay un requisito para determinar la contraseña correcta de un array de contraseñas y abrir el documento con la contraseña correcta. El siguiente fragmento de código demuestra los pasos para iterar a través del array de contraseñas e intentar abrir el documento con la contraseña correcta.

```java
public static void DetermineCorrectPasswordFromArray() {
     // Cargar el archivo PDF de origen
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // Determinar si el PDF de origen está cifrado
   System.out.println("El archivo está protegido por contraseña " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("El número de páginas en el documento es = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("La contraseña = " + passwords[passwordcount] + " no es correcta");
    }
   }
```