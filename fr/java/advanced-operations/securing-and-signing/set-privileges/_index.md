---
title: Définir des Privilèges, Chiffrer et Déchiffrer un Fichier PDF 
linktitle: Chiffrer et Déchiffrer un Fichier PDF
type: docs
weight: 20
url: fr/java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: chiffrer pdf,protéger par mot de passe pdf,déchiffrer pdf,java
description: Chiffrer un Fichier PDF avec Java en utilisant Différents Types et Algorithmes de Chiffrement. Aussi, déchiffrer des Fichiers PDF en utilisant le Mot de Passe Propriétaire.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Définir des Privilèges sur un Fichier PDF Existant

Pour définir des privilèges sur un fichier PDF, créez un objet de la classe DocumentPrivilege et spécifiez les droits que vous souhaitez appliquer au document.
 Une fois que les privilèges ont été définis, passez cet objet en argument à la méthode [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Le snippet de code suivant vous montre comment définir les privilèges d'un fichier PDF.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // Charger un fichier PDF source
   Document document = new Document(_dataDir + "input.pdf");

   // Instancier un objet Document Privileges
   // Appliquer des restrictions sur tous les privilèges
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Autoriser uniquement la lecture à l'écran
   documentPrivilege.setAllowScreenReaders(true);
   // Chiffrer le fichier avec un mot de passe utilisateur et propriétaire.
   // Besoin de définir le mot de passe, afin que lorsque l'utilisateur consulte le fichier avec le mot de passe utilisateur,
   // Seule l'option de lecture à l'écran est activée
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Enregistrer le document mis à jour
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Chiffrer un fichier PDF en utilisant différents types et algorithmes de chiffrement

Vous pouvez utiliser la méthode [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) pour chiffrer un fichier PDF. Vous pouvez passer le mot de passe utilisateur, le mot de passe propriétaire et les permissions à la méthode [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-). En plus de cela, vous pouvez passer n'importe quelle valeur de l'énumération [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm). Cette énumération fournit différentes combinaisons d'algorithmes de chiffrement et de tailles de clés. Vous pouvez passer la valeur de votre choix. Enfin, enregistrez le fichier PDF chiffré en utilisant la méthode [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

>Veuillez spécifier des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

The following code snippet shows you how to encrypt PDF files.

```java
public static void EncryptPDFFile() {
   // Charger un fichier PDF source
   Document document = new Document(_dataDir + "input.pdf");

   // Instancier un objet Document Privileges
   // Appliquer des restrictions sur tous les privilèges
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Permettre uniquement la lecture à l'écran
   documentPrivilege.setAllowScreenReaders(true);
   // Chiffrer le fichier avec un mot de passe utilisateur et propriétaire.
   // Besoin de définir le mot de passe, afin qu'une fois que l'utilisateur
   // visualise le fichier avec le mot de passe utilisateur,
   // Seule l'option de lecture à l'écran est activée
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Enregistrer le document mis à jour
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Décrypter un fichier PDF en utilisant le mot de passe propriétaire

Pour décrypter le fichier PDF, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et ouvrir le PDF en utilisant le mot de passe propriétaire.
 Après cela, vous devez appeler la méthode [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). L'extrait de code suivant vous montre comment décrypter le fichier PDF.

```java
public static void DecryptPDFFile() {
   // Ouvrir le document
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // Décrypter PDF
   document.decrypt();

   // Enregistrer le PDF mis à jour
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## Changer le mot de passe d'un fichier PDF

Si vous souhaitez changer le mot de passe d'un fichier PDF, vous devez d'abord ouvrir le fichier PDF en utilisant le mot de passe propriétaire avec l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Après cela, vous devez appeler la méthode [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Vous devez passer le mot de passe propriétaire actuel ainsi que le nouveau mot de passe utilisateur et le nouveau mot de passe propriétaire à cette méthode. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le code suivant vous montre comment changer le mot de passe d'un fichier PDF.

```java
public static void ChangePassword_PDF_File() {
   // Ouvrir le document
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // Changer le mot de passe
   document.changePasswords("owner", "newuser", "newowner");
   // Enregistrer le PDF mis à jour
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## Comment - déterminer si le PDF source est protégé par un mot de passe

Aspose.PDF pour Java offre de grandes capacités de gestion des documents PDF. Lorsque vous utilisez la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) du package com.aspose.pdf pour ouvrir un document PDF protégé par mot de passe, nous devons fournir les informations de mot de passe comme argument au constructeur Document et dans le cas où ces informations ne sont pas fournies, un message d'erreur est généré. En fait, lorsque vous essayez d'ouvrir un fichier PDF avec un objet Document, le constructeur essaie de lire le contenu du fichier PDF et dans le cas où le mot de passe correct n'est pas fourni, un message d'erreur est généré (cela se produit pour empêcher l'accès non autorisé au document).

Lorsque vous traitez des fichiers PDF cryptés, vous pouvez rencontrer le scénario où vous seriez intéressé à détecter si un PDF a un mot de passe d'ouverture et/ou un mot de passe de modification. Parfois, il existe des documents qui ne nécessitent pas d'informations de mot de passe lors de leur ouverture, mais ils nécessitent des informations pour modifier le contenu du fichier. Donc, afin de répondre aux exigences ci-dessus, la classe PdfFileInfo présente dans le package com.aspose.pdf.facades fournit des méthodes qui peuvent aider à déterminer les informations requises.

### Obtenir des informations sur la sécurité du document PDF

PdfFileInfo contient trois méthodes pour obtenir des informations sur la sécurité du document PDF.

1. La méthode getPasswordType() renvoie une valeur d'énumération PasswordType :
    1. PasswordType.None - le document n'est pas protégé par mot de passe
    1. PasswordType.User - le document a été ouvert avec le mot de passe utilisateur (ou ouverture du document)
    1. PasswordType.Owner - le document a été ouvert avec le mot de passe propriétaire (ou permissions, édition)
    1. PasswordType.Inaccessible - le document est protégé par mot de passe mais un mot de passe est nécessaire pour l'ouvrir alors qu'un mot de passe invalide (ou aucun mot de passe) a été fourni.
1. La méthode hasOpenPassword() est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe lors de son ouverture.
1. La méthode hasEditPassword() est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe pour modifier son contenu.

### Déterminer le mot de passe correct à partir d'un tableau

Parfois, il est nécessaire de déterminer le mot de passe correct à partir d'un tableau de mots de passe et d'ouvrir le document avec le mot de passe correct. Le code suivant illustre les étapes pour parcourir le tableau de mots de passe et essayer d'ouvrir le document avec le mot de passe correct.

```java
public static void DetermineCorrectPasswordFromArray() {
     // Charger le fichier PDF source
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // Déterminer si le PDF source est chiffré
   System.out.println("Le fichier est protégé par mot de passe " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("Le nombre de pages dans le document est = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("Le mot de passe = " + passwords[passwordcount] + " n'est pas correct");
    }
   }
```