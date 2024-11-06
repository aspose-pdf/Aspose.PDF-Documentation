---
title: Как цифрово подписать PDF
linktitle: Цифровая подпись PDF
type: docs
weight: 10
url: ru/cpp/digitally-sign-pdf-file/
description: Цифровая подпись PDF документов с использованием C++. Проверка или валидация цифрово подписанных PDF с использованием C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Подпись PDF с помощью цифровых подписей

Вы можете подписать PDF-документ, чтобы подтвердить его содержимое, или вы можете утвердить документ с помощью Aspose.PDF.

Aspose.PDF для C++ поддерживает функцию цифровой подписи PDF-файлов с использованием класса SignatureField. Вы также можете сертифицировать PDF-файл с помощью PKCS12-сертификата. Что-то аналогичное [Добавление подписей и безопасности в Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6). 

Используйте класс [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) для подписи вашего PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// Строка для имени пути.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Используйте PKCS7/PKCS7Detached
























// объекты

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// Сохраните выходной PDF файл

signature->Save(outFile);
}
```

## Добавить временную метку к цифровой подписи

### Как подписать PDF с временной меткой

Aspose.PDF для C++ поддерживает цифровую подпись PDF с использованием сервера временных меток или веб-сервиса.

Временные метки используются для указания даты и времени, когда вы подписали документ. Надежное временное штампование доказывает, что содержимое ваших PDF существовало в определенный момент времени и не изменялось с тех пор.

Используйте класс [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) для добавления доверенной временной метки к цифровым подписям или документам.

Пожалуйста, ознакомьтесь с следующим кодом, который получает временную метку и добавляет ее в PDF документ:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {

// Строка для имени пути.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);

auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");

auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // Пользователь/Пароль могут быть опущены

pkcs->set_TimestampSettings(timestampSettings);

System::Drawing::Rectangle rect(100, 100, 200, 100);

// Создайте любой из трех типов подписи

signature->Sign(1, u"Signature Reason", u"Contact", u"Location", true, rect, pkcs);

// Сохраните выходной PDF файл

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```