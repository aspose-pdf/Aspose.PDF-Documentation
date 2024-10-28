---
title: Crypter un fichier PDF
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: Ce sujet explique comment crypter un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Crypter un document PDF protège son contenu contre tout accès non autorisé de l'extérieur, surtout lors du partage ou de l'archivage de fichiers.

Les documents PDF confidentiels peuvent être cryptés et protégés par mot de passe. Seul l'utilisateur qui connaît le mot de passe pourra décrypter, ouvrir et visualiser ces documents.

Voyons comment le cryptage PDF fonctionne avec la bibliothèque Aspose.PDF.

## Crypter un fichier PDF en utilisant différents types et algorithmes de cryptage

Afin de crypter un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) puis appeler la méthode [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Vous pouvez passer le mot de passe utilisateur, le mot de passe propriétaire et les privilèges à la méthode [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Vous devez également passer les valeurs KeySize et Algorithm à cette méthode.

Passez en revue une liste possible de tels [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) :

|**Nom du membre**|**Valeur**|**Description**|
| :- | :- | :- |
|RC4x40|0|RC4 avec une longueur de clé de 40.|
|RC4x128|1|RC4 avec une longueur de clé de 128.|
|AESx128|2|AES avec une longueur de clé de 128.|
|AESx256|3|AES avec une longueur de clé de 256.|

L'extrait de code suivant vous montre comment crypter un fichier PDF.

```csharp
public static void EncryptPDFFile()
        {
            // Créer un objet PdfFileSecurity
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // Crypter le fichier en utilisant le cryptage 256 bits
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```