---
title: Définir les privilèges, chiffrer et déchiffrer un fichier PDF en utilisant C++
linktitle: Chiffrer et déchiffrer un fichier PDF
type: docs
weight: 20
url: /fr/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: chiffrer pdf,protéger pdf par mot de passe,déchiffrer pdf,c++
description: Chiffrer un fichier PDF avec C++ en utilisant différents types et algorithmes de chiffrement. De plus, déchiffrer des fichiers PDF en utilisant le mot de passe du propriétaire.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Définir les privilèges sur un fichier PDF existant

Pour définir des privilèges sur un fichier PDF existant, Aspose.PDF pour C++ utilise la classe [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) et spécifie les droits que vous souhaitez appliquer au document. Une fois les privilèges définis, passez cet objet en tant qu'argument à la méthode [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Le fragment de code suivant vous montre comment définir les privilèges d'un fichier PDF.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Charger un fichier PDF source
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instancier l'objet Privileges Document

    // Appliquer des restrictions sur tous les privilèges
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Autoriser uniquement la lecture d'écran
    documentPrivilege->set_AllowScreenReaders(true);

    // Chiffrer le fichier avec un mot de passe utilisateur et propriétaire.
    // Besoin de définir le mot de passe, afin que l'utilisateur puisse voir le fichier avec le mot de passe utilisateur,

    // Seule l'option de lecture d'écran est activée
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Chiffrer un fichier PDF en utilisant différents types et algorithmes de chiffrement

Pour chiffrer un fichier PDF, utilisez la méthode [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) pour chiffrer un fichier PDF.

Le code suivant vous montre comment chiffrer des fichiers PDF.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // Chaîne pour le nom de chemin.
    String _dataDir("C:\\Samples\\");

    // Charger un fichier PDF source
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instancier l'objet de privilèges de document
    // Appliquer des restrictions sur tous les privilèges
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Autoriser uniquement la lecture sur écran
    documentPrivilege->set_AllowScreenReaders(true);
    // Chiffrer le fichier avec le mot de passe utilisateur et propriétaire.
    // Besoin de définir le mot de passe, afin qu'une fois que l'utilisateur visualise le fichier avec le mot de passe utilisateur,
    // Seule l'option de lecture sur écran est activée
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Déchiffrer le fichier PDF en utilisant le mot de passe propriétaire

Pour déchiffrer le fichier PDF, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) et ouvrir le PDF en utilisant le mot de passe du propriétaire. Après cela, vous devez appeler la méthode [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a).

```cpp
void SecuringAndSigning::DecryptPDFFile() {

// Chaîne pour le nom du chemin.

String _dataDir("C:\\Samples\\");


// Ouvrir le document

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// Décrypter le PDF

document->Decrypt();


// Enregistrer le PDF mis à jour

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## Changer le mot de passe d'un fichier PDF

Étant donné que vos PDF peuvent contenir des informations importantes et confidentielles, ils doivent rester en sécurité. En conséquence, vous pourriez avoir besoin de changer le mot de passe de votre document PDF.

Si vous souhaitez changer le mot de passe d'un fichier PDF, vous devez d'abord ouvrir le fichier PDF en utilisant le mot de passe propriétaire avec l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Après cela, vous devez appeler la méthode [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d).


Le snippet de code suivant vous montre comment changer le mot de passe d'un fichier PDF.
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

## Comment - déterminer si le PDF source est protégé par un mot de passe

Un document PDF crypté avec le mot de passe de l'utilisateur ne peut pas être ouvert sans un mot de passe. Nous ferions mieux de déterminer si le document est protégé par mot de passe avant d'essayer de l'ouvrir. Parfois, il y a des documents qui ne nécessitent pas d'informations de mot de passe lors de leur ouverture, mais qui nécessitent des informations pour modifier le contenu du fichier. Donc, pour répondre aux exigences ci-dessus, la classe [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) présente sous Aspose.PDF.Facades fournit les propriétés qui peuvent aider à déterminer les informations requises.

### Obtenir des informations sur la sécurité du document PDF

PdfFileInfo contient trois propriétés pour obtenir des informations sur la sécurité du document PDF.

1. la propriété PasswordType renvoie la valeur d'énumération PasswordType :
    - PasswordType.None - le document n'est pas protégé par mot de passe
    - PasswordType.User - le document a été ouvert avec un mot de passe utilisateur (ou d'ouverture de document)
    - PasswordType.Owner - le document a été ouvert avec un mot de passe propriétaire (ou de permissions, édition)

    - PasswordType.Inaccessible - le document est protégé par mot de passe mais le mot de passe est nécessaire pour l'ouvrir alors qu'un mot de passe invalide (ou aucun mot de passe) a été fourni.2. propriété booléenne HasOpenPassword - est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe pour l'ouvrir.
3. propriété booléenne HasEditPassword - est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe pour modifier son contenu.

### Déterminer le mot de passe correct à partir d'un tableau

Parfois, il est nécessaire de déterminer le mot de passe correct à partir d'un tableau de mots de passe et d'ouvrir le document avec le mot de passe correct. Le code suivant démontre les étapes pour parcourir le tableau de mots de passe et essayer d'ouvrir le document avec le bon mot de passe.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// Chaîne pour le nom du chemin.

String _dataDir("C:\\Samples\\");


// Charger le fichier PDF source

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// Déterminer si le PDF source est chiffré

Console::WriteLine(u"Le fichier est protégé par mot de passe {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"Le nombre de pages dans le document est = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"Le mot de passe = {0} n'est pas correct", passwords[passwordcount]);


}

}

Console::WriteLine(u"Test terminé");
}
```