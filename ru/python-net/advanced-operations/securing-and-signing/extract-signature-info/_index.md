---
title: Извлечь информацию о подписи из PDF на Python
linktitle: Извлечь детали из подписи
type: docs
weight: 20
url: /python-net/extract-image-and-signature-information/
description: Узнайте, как извлекать изображения подписей, сертификаты и детали цифровой подписи из PDF‑файлов на Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Извлекайте изображения подписей и детали сертификатов из PDF‑файлов на Python
Abstract: Эта статья объясняет, как извлекать информацию об изображениях и цифровой подписи из PDF‑документов с помощью Aspose.PDF for Python. Узнайте, как получать изображения подписи, извлекать данные сертификата, просматривать алгоритмы подписи и обнаруживать скомпрометированные подписи в подписанных PDF‑файлах.
---

## Извлечь изображение из поля подписи

Aspose.PDF for Python via .NET позволяет вам получить визуальное изображение, встроенное в [ПолеПодписи](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Это полезно, когда вам нужно отобразить или архивировать внешний вид подписи без рендеринга полного PDF.

Пример ниже перебирает все поля формы, находя каждое `SignatureField`, и сохраняет его изображение в файл JPEG:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## Прочитать детали алгоритма подписи

Использовать `PdfFileSignature.get_signatures_info()` чтобы прочитать криптографические метаданные для каждой подписи в документе — включая алгоритм дайджеста, тип алгоритма, криптографический стандарт и имя подписи:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## Извлечь цифровой сертификат из поля подписи

Использовать [извлечь_сертификат](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) метод на a `SignatureField` чтобы получить встроенный сертификат в виде потока байтов и сохранить его на диск для внешней проверки:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## Извлечение сертификатов с использованием фасада PdfFileSignature

`PdfFileSignature.try_extract_certificate()` предоставляет альтернативный способ получения сертификатов по имени подписи. Следующий пример перебирает все имена подписи и пытается выполнить извлечение для каждого:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## Проверить внешние цифровые подписи

Чтобы подтвердить, что документ не был изменён после подписания, проверьте каждую внешнюю подпись, используя `PdfFileSignature.verify_signature()`. Пример ниже генерирует исключение для любой подписи, не прошедшей проверку:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Обнаружить скомпрометированные подписи

`SignaturesCompromiseDetector` проверяет, были ли какие‑либо цифровые подписи в документе аннулированы последующими изменениями. Используйте это в юридических, финансовых или комплаенс‑процессах, где необходимо гарантировать целостность документа.

Пример ниже проверяет компрометированные подписи и выводит их имена вместе с общей охватом подписей в документе:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## Связанные темы безопасности

- [Защищайте и подписывайте PDF‑файлы на Python](/pdf/ru/python-net/securing-and-signing/)
- [Электронно подписать PDF‑файлы в Python](/pdf/ru/python-net/digitally-sign-pdf-file/)
- [Подписать PDF-документы со смарт-картой в Python](/pdf/ru/python-net/sign-pdf-document-from-smart-card/)
- [Шифрование и дешифрование PDF-файлов в Python](/pdf/ru/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
