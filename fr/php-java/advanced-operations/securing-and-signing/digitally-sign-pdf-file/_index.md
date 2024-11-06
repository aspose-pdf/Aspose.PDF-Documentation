---
title: Comment signer numériquement un PDF
linktitle: Signer numériquement un PDF
type: docs
weight: 10
url: fr/php-java/digitally-sign-pdf-file/
description: Signez numériquement des documents PDF en utilisant Java. Vérifiez ou validez les PDF signés numériquement avec une application basée sur Java utilisant la bibliothèque PDF. Vous pouvez certifier un fichier PDF avec un certificat PKCS1.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Lorsque vous signez un document PDF avec une signature, vous confirmez essentiellement que son contenu doit rester "en l'état". Par conséquent, toute modification effectuée par la suite invalide la signature et ainsi, vous savez si le document a été modifié. Certifier d'abord un document vous permet de spécifier les modifications qu'un utilisateur peut apporter au document sans invalider la certification.

En d'autres termes, le document serait toujours considéré comme conservant son intégrité et le destinataire pourrait toujours faire confiance au document. Pour plus de détails, veuillez visiter Certifying and signing a PDF.

## Signer un PDF avec des signatures numériques

```php

    // Ouvrir le document
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // Utiliser PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // Enregistrer le fichier PDF de sortie
    $signature->save($outputFile);    
    $document->close();
```