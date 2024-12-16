---
title: Como assinar PDF digitalmente
linktitle: Assinar PDF Digitalmente
type: docs
weight: 10
url: /pt/php-java/digitally-sign-pdf-file/
description: Assine digitalmente documentos PDF usando Java. Verifique ou valide PDFs assinados digitalmente com aplicativo baseado em Java com PDF Library. Você pode certificar um arquivo PDF com um Certificado PKCS1.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Ao assinar um documento PDF usando uma assinatura, você basicamente confirma que seu conteúdo deve permanecer "como está". Consequentemente, quaisquer alterações feitas posteriormente invalidam a assinatura e, assim, você sabe se o documento foi alterado. Certificar um documento primeiro permite que você especifique as alterações que um usuário pode fazer no documento sem invalidar a certificação.

Em outras palavras, o documento ainda seria considerado para manter sua integridade e o destinatário ainda poderia confiar no documento. Para mais detalhes, por favor visite Certificação e assinatura de um PDF.

## Assinar PDF com assinaturas digitais

```php

    // Abrir documento
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // Use PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // Salvar arquivo PDF de saída
    $signature->save($outputFile);    
    $document->close();
```