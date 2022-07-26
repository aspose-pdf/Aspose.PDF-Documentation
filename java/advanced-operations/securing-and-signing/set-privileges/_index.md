---
title: Set Privileges, Encrypt and Decrypt PDF File 
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 20
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: encrypt pdf,password protect pdf,decrypt pdf,java
description: Encrypt PDF File with Java using Different Encryption Types and Algorithms. Also, decrypt PDF Files using Owner Password.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Set Privileges on an Existing PDF File

To set privileges on a PDF file, create an object of the DocumentPrivilege class and specify the rights you want to apply to the document. Once the privileges have been defined, pass this object as an argument to the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) method. The following code snippet shows you how to set the privileges of a PDF file.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // Load a source PDF file
   Document document = new Document(_dataDir + "input.pdf");

   // Instantiate Document Privileges object
   // Apply restrictions on all privileges
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Only allow screen reading
   documentPrivilege.setAllowScreenReaders(true);
   // Encrypt the file with User and Owner password.
   // Need to set the password, so that once the user views the file with user password,
   // Only screen reading option is enabled
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Save updated document
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Encrypt PDF File using Different Encryption Types and Algorithms

You can use the [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object to encrypt a PDF file. You can pass the user password, owner password, and permissions to the [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) method. In addition to that, you can pass any value of the [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm) enum. This enum provides different combinations of encryption algorithms and key sizes. You can pass the value of your choice. Finally, save the encrypted PDF file using [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.

>Please specify different user and owner passwords while encrypting the PDF file.

The following code snippet shows you how to encrypt PDF files.

```java
public static void EncryptPDFFile() {
   // Load a source PDF file
   Document document = new Document(_dataDir + "input.pdf");

   // Instantiate Document Privileges object
   // Apply restrictions on all privileges
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Only allow screen reading
   documentPrivilege.setAllowScreenReaders(true);
   // Encrypt the file with User and Owner password.
   // Need to set the password, so that once the user views the file with user
   // password,
   // Only screen reading option is enabled
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Save updated document
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Decrypt PDF File using Owner Password

In order to decrypt the PDF file, you first need to create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and open the PDF using the owner’s password. After that, you need to call [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)  object. Finally, save the updated PDF file using Save method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)  object. The following code snippet shows you how to decrypt the PDF file.

```java
public static void DecryptPDFFile() {
   // Open document
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // Decrypt PDF
   document.decrypt();

   // Save updated PDF
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## Change Password of a PDF File

If you want to change the password of a PDF file, you first need to open the PDF file using owner password with the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object. After that, you need to call the [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object. You need to pass the current owner password along with the new user password and new owner password to this method. Finally, save the updated PDF file using Save method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)  object.

The following code snippet shows you how to change the password of a PDF file.

```java
public static void ChangePassword_PDF_File() {
   // Open document
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // Change password
   document.changePasswords("owner", "newuser", "newowner");
   // Save updated PDF
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## How to - determine if the source PDF is password protected

Aspose.PDF for Java provides great capabilities of dealing with PDF documents. When using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class of com.aspose.pdf package to open a PDF document which is password protected, we need to provide the password information as an argument to Document constructor and in case this information is not provided, an error message is generated. In fact when trying to open a PDF file with Document object, the constructor is trying to read the contents of PDF file and in case correct password is not provided, an error message is generated (it happens to prevent unauthorised access of document)

When dealing with encrypted PDF files, you may come across the scenario where you would be interested to detect if a PDF has an open password and/or an edit password. Sometimes there are documents which do not require password information while opening them, but they require information in order to edit the contents of file.. So in order to fulfil the above requirements, PdfFileInfo class present under com.aspose.pdf.facades package provides the methods which can help in determining the required information.

### Get information about PDF document security

PdfFileInfo contains three methods to get information about PDF document security.

1. getPasswordType() method returns PasswordType enumeration value:
    1. PasswordType.None - document is not password protected
    1. PasswordType.User - document was opened with user (or document open) password
    1. PasswordType.Owner - document was opened with owner (or permissions, edit) password
    1. PasswordType.Inaccessible - document is password protected but password is needed to open it while invalid password (or no password) was supplied.
1. hasOpenPassword() method is used to determine if input file requires password, when opening it.
1. hasEditPassword() method is used to determine if input file requires password to edit its contents.

### Determine correct password from Array

Sometimes there is a requirement to determine the correct password from an array of passwords and open the document with the correct password. The following code snippet demonstrates the steps to iterate through the array of passwords and try opening the document with the correct password.

```java
public static void DetermineCorrectPasswordFromArray() {
     // Load source PDF file
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // Determine if the source PDF is encrypted
   System.out.println("File is password protected " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("Number of Page in document are = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("Password = " + passwords[passwordcount] + "  is not correct");
    }
   }
```
