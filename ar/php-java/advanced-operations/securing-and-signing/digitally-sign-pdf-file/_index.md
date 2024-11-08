---
title: كيفية توقيع PDF رقميًا
linktitle: التوقيع الرقمي PDF
type: docs
weight: 10
url: /ar/php-java/digitally-sign-pdf-file/
description: توقيع مستندات PDF رقميًا باستخدام Java. تحقق أو تحقق من التوقيعات الرقمية لـ PDF باستخدام تطبيق قائم على Java مع مكتبة PDF. يمكنك اعتماد ملف PDF بشهادة PKCS1.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

عند توقيع مستند PDF باستخدام توقيع، فإنك تؤكد بشكل أساسي أن محتوياته يجب أن تظل "كما هي". وبالتالي، أي تغييرات تُجرى بعد ذلك تجعل التوقيع غير صالح، وهكذا تعرف ما إذا تم تغيير المستند. يتيح لك اعتماد مستند أولاً تحديد التغييرات التي يمكن للمستخدم إجراؤها على المستند دون إبطال الاعتماد.

بمعنى آخر، سيظل يُعتبر المستند يحتفظ بسلامته ويمكن للمستلم أن يثق في المستند. لمزيد من التفاصيل، يرجى زيارة اعتماد وتوقيع PDF.

## توقيع PDF بالتوقيعات الرقمية

```php

    // فتح المستند
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // استخدم PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // حفظ ملف PDF الناتج
    $signature->save($outputFile);    
    $document->close();
```