---
title: Set Privileges,Encrypt and Decrypt PDF File 
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 20
url: /cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encrypt PDF File using Different Encryption Types and Algorithms. Also, decrypt PDF File using Owner Password.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Set Privileges on an Existing PDF File

For setting privileges on an existing PDF file Aspose.PDF for C++ use [DocumentPrivilege](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) class and specify the rights you want to apply to the document. Once the privileges have been defined, pass this object as an argument to the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object’s [Encrypt](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) method.

The following code snippet shows you how to set the privileges of a PDF file.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
	// String for path name.
	String _dataDir("C:\\Samples\\");

	// Load a source PDF file
	auto document = MakeObject<Document>(_dataDir + u"input.pdf");

	// Instantiate Document Privileges object

	// Apply restrictions on all privileges
	auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
	// Only allow screen reading
	documentPrivilege->set_AllowScreenReaders(true);

	// Encrypt the file with User and Owner password.
	// Need to set the password, so that once the user views the file with user password,

	// Only screen reading option is enabled
	document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

	// Save updated document
	document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Encrypt PDF File using Different Encryption Types and Algorithms

For the encrypting PDF file use [Encrypt](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) method of the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object to encrypt a PDF file. 

The following code snippet shows you how to encrypt PDF files.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
	// String for path name.
	String _dataDir("C:\\Samples\\");

	// Load a source PDF file
	auto document = MakeObject<Document>(_dataDir + u"input.pdf");

	// Instantiate Document Privileges object
	// Apply restrictions on all privileges
	auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
	// Only allow screen reading
	documentPrivilege->set_AllowScreenReaders(true);
	// Encrypt the file with User and Owner password.
	// Need to set the password, so that once the user views the file with user
	// password,
	// Only screen reading option is enabled
	document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
	// Save updated document
	document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Decrypt PDF File using Owner Password

In order to decrypt the PDF file, you first need to create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object and open the PDF using the owner’s password. After that, you need to call [Decrypt](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a) method.

```cpp
void SecuringAndSigning::DecryptPDFFile() {

	// String for path name.
	String _dataDir("C:\\Samples\\");

	// Open document
	auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");
	// Decrypt PDF
	document->Decrypt();

	// Save updated PDF
	document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## Change Password of a PDF File

Since your PDFs can carry important and confidential information, they must remain safe. Accordingly, you may need to change password of your PDF document.

If you want to change the password of a PDF file, you first need to open the PDF file using owner password with the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object. After that, you need to call the [ChangePasswords](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d) method.

The following code snippet shows you how to change the password of a PDF file.

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

## How to - determine if the source PDF is password protected

A PDF document encrypted with the user's password cannot be opened without a password. We'd better determine if the document is password protected before we try to open it. Sometimes there are documents that do not require password information while opening them, but they require information in order to edit the contents of the file. So in order to fulfill the above requirements, [PdfFileInfo](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) class present under Aspose.PDF.Facades provides the properties which can help in determining the required information.

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

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {

	// String for path name.
	String _dataDir("C:\\Samples\\");

	// Load source PDF file
	auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");

	// Determine if the source PDF is encrypted
	Console::WriteLine(u"File is password protected {0}", info->get_IsEncrypted());
	const int count = 5;
	String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };

	for (int passwordcount = 0; passwordcount < count; passwordcount++)
	{
		try
		{
			auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);
			auto pages = document->get_Pages()->get_Count();
			if (pages > 0)
				Console::WriteLine(u"Number of Page in document are = {0}", pages);
		}
		catch (Aspose::Pdf::InvalidPasswordException ex)
		{
			Console::WriteLine(u"Password = {0} is not correct", passwords[passwordcount]);
		}
	}
	Console::WriteLine(u"Test finished");
}
```
