---
title: Set Privileges,Encrypt and Decrypt PDF File 
type: docs
weight: 20
url: /net/set-privileges-encrypt-and-decrypt-pdf-file/
---
# Set Privileges,Encrypt and Decrypt PDF File
## Set Privileges on an Existing PDF File
To set privileges on a PDF file, create an object of the [DocumentPrivilege](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege)class and specify the rights you want to apply to the document. Once the privileges have been defined, pass this object as an argument to the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object’s Encrypt(..) method. The following code snippet shows you how to set the privileges of a PDF file.
```cshrap
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Load a source PDF file
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Instantiate Document Privileges object
    // Apply restrictions on all privileges
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Only allow screen reading
    documentPrivilege.AllowScreenReaders = true;
    // Encrypt the file with User and Owner password.
    // Need to set the password, so that once the user views the file with user password,
    // Only screen reading option is enabled
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Save updated document
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```

## Encrypt PDF File using Different Encryption Types and Algorithms
You can use the [Encrypt](https://apireference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object to encrypt a PDF file. You can pass the user password, owner password, and permissions to the [Encrypt](https://apireference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) method. In addition to that, you can pass any value of the [CryptoAlgorithm](https://apireference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) enum. This enum provides different combinations of encryption algorithms and key sizes. You can pass the value of your choice. Finally, save the encrypted PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.

>Please specify different user and owner passwords while encrypting the PDF file.

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it’s not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The following code snippet shows you how to encrypt PDF files.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Open document
Document document = new Document(dataDir+ "Encrypt.pdf");
// Encrypt PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// Save updated PDF
document.Save(dataDir);
```
## Decrypt PDF File using Owner Password
In order to decrypt the PDF file, you first need to create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object and open the PDF using the owner’s password. After that, you need to call [Decrypt](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object. Finally, save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object. The following code snippet shows you how to decrypt the PDF file.

```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Open document
Document document = new Document(dataDir+ "Decrypt.pdf", "password");
// Decrypt PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// Save updated PDF
document.Save(dataDir);
```
## Change Password of a PDF File 
If you want to change the password of a PDF file, you first need to open the PDF file using owner password with the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object. After that, you need to call the [ChangePasswords](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object. You need to pass the current owner password along with the new user password and new owner password to this method. Finally, save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document)  object.

>- The User password, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it’s not correct, the document will not open. 
>- The Owner password, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The following code snippet shows you how to change the password of a PDF file.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Open document
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// Change password
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// Save updated PDF
document.Save(dataDir);
```
## How to - determine if the source PDF is password protected
**Aspose.PDF for .NET** provides great capabilities of dealing with PDF documents. When using Document class of Aspose.PDF namespace to open a PDF document that is password-protected, we need to provide the password information as an argument to Document constructor and in case this information is not provided, an error message is generated. In fact, when trying to open a PDF file with Document object, the constructor is trying to read the contents of PDF file and in case correct password is not provided, an error message is generated (it happens to prevent unauthorized access of document)

When dealing with encrypted PDF files, you may come across the scenario where you would be interested to detect if a PDF has an open password and/or an edit password. Sometimes there are documents that do not require password information while opening them, but they require information in order to edit the contents of the file. So in order to fulfill the above requirements, PdfFileInfo class present under Aspose.PDF.Facades provides the properties which can help in determining the required information.

### Get information about PDF document security
PdfFileInfo contains three properties to get information about PDF document security.

1. property PasswordType returns PasswordType enumeration value:
- PasswordType.None - the document is not password protected
- PasswordType.User - the document was opened with user (or document open) password
- PasswordType.Owner - the document was opened with owner (or permissions, edit) password
- PasswordType.Inaccessible - the document is password protected but the password is needed to open it while an invalid password (or no password) was supplied.
2. boolean property HasOpenPassword - is used to determine if the input file requires a password, when opening it.
3. boolean property HasEditPassword - its used to determine if the input file requires a password to edit its contents.

### Determine correct password from Array
Sometimes there is a requirement to determine the correct password from an array of passwords and open the document with the correct password. The following code snippet demonstrates the steps to iterate through the array of passwords and try opening the document with the correct password.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();            
// Load source PDF file
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Determine if the source PDF is encrypted
Console.WriteLine("File is password protected " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Number of Page in document are = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
    }
}
```
