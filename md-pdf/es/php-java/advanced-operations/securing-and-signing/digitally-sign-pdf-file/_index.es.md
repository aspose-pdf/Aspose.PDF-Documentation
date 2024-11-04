---
title: Cómo firmar digitalmente un PDF
linktitle: Firmar digitalmente PDF
type: docs
weight: 10
url: /php-java/digitally-sign-pdf-file/
description: Firmar digitalmente documentos PDF usando Java. Verificar o validar los PDFs firmados digitalmente con una aplicación basada en Java con PDF Library. Puede certificar un archivo PDF con un Certificado PKCS1.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Al firmar un documento PDF usando una firma, básicamente confirmas que su contenido debe permanecer "como está". En consecuencia, cualquier cambio realizado posteriormente invalida la firma y, por lo tanto, sabes si el documento ha sido alterado. Certificar un documento primero, te permite especificar los cambios que un usuario puede hacer al documento sin invalidar la certificación.

En otras palabras, el documento aún se consideraría que mantiene su integridad y el destinatario aún podría confiar en el documento. Para más detalles, por favor visita Certificando y firmando un PDF.

## Firmar PDF con firmas digitales

```php

    // Abrir documento
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // Usar PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // Guardar archivo PDF de salida
    $signature->save($outputFile);    
    $document->close();
```