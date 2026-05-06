---
title: Добавить цифровую подпись или подписать PDF в Python
linktitle: Подписать PDF цифровой подписью
type: docs
weight: 10
url: /ru/python-net/digitally-sign-pdf-file/
description: Узнайте, как подписывать цифровой подписью PDF‑документы, добавлять метки времени и проверять подписи в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Подписывайте цифровой подписью PDF‑файлы с помощью Python.
Abstract: Это руководство объясняет, как подписывать цифровой подписью PDF‑документы с помощью Aspose.PDF for Python via .NET. В нём подробно описан процесс применения стандартных и продвинутых цифровых подписей, использование сертификатов (PFX и PKCS#12) и настройка внешнего вида и поведения подписи. Документация содержит примеры кода, демонстрирующие, как подписывать существующие PDF, добавлять метки времени и проверять валидность подписи. Это позволяет разработчикам обеспечивать подлинность, целостность документов и соответствие стандартам цифровой подписи в их Python‑приложениях.
---

## Подписать PDF с помощью цифровых подписей

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

Подпись **PKCS#7 detached signature** добавляет цифровую подпись к документу, не встраивая содержимое в блок подписи.

Используйте эти примеры, когда вам нужно применять подписи на основе сертификата к PDF‑файлам, проверять действительность подписи или добавлять доверенные временные метки к подписанным документам.

Следующий пример подписывает PDF‑документ, используя отдельную цифровую подпись PKCS#7, применяя подпись к первой странице в указанной прямоугольной области.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Проверьте все цифровые подписи в PDF‑документе**

1. Создает экземпляр PdfFileSignature, который позволяет взаимодействовать с подписями в PDF.
1. Получите список имен подписей `get_signature_names(True)`.
1. Проверяет первую подпись в списке `verify_signature` для соответствия указанному сертификату.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**Проверить подпись с использованием файла сертификата открытого ключа**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**Проверьте подпись с сертификатом, извлечённым из файла**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**Проверка подписей с включённой проверкой цепочки сертификатов**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## Добавить метку времени к цифровой подписи

### Как подписать цифровой подписью PDF с отметкой времени

Aspose.PDF for Python поддерживает цифровую подпись PDF с использованием сервера меток времени или веб‑сервиса.

Для выполнения этого требования, [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) класс был добавлен в пространство имен Aspose.PDF. Пожалуйста, посмотрите следующий фрагмент кода, который получает метку времени и добавляет её в PDF‑документ:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## Подписание PDF‑документов с использованием ECDSA

Подписание PDF‑документов с использованием ECDSA (Эллиптический алгоритм цифровой подписи) подразумевает применение криптографии эллиптических кривых для создания цифровых подписей.

Приведённый выше фрагмент кода демонстрирует, как применить отдельную (detached) цифровую подпись PKCS#7 к документу PDF с использованием Aspose.PDF for Python. Загрузив документ, настроив внешний вид подписи и параметры безопасности, а затем сохранив результат, данный пример показывает полный, надёжный процесс цифровой подписи PDF‑файлов.

Этот метод обеспечивает подлинность и целостность документа, внедряя безопасную, проверяемую подпись на первой странице. Использование SHA-256 в качестве алгоритма хеширования соответствует современным криптографическим стандартам, а возможность управлять размещением подписи предоставляет гибкость для видимых отметок одобрения.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Проверить подписи ECDSA в PDF‑документе**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Связанные темы безопасности

- [Обеспечьте безопасность и подпишите PDF‑файлы с помощью Python](/pdf/ru/python-net/securing-and-signing/)
- [Извлечь информацию об изображении и подписи в Python](/pdf/ru/python-net/extract-image-and-signature-information/)
- [Подписать PDF‑документы со смарт‑карты в Python](/pdf/ru/python-net/sign-pdf-document-from-smart-card/)
- [Шифрование и расшифровка PDF‑файлов в Python](/pdf/ru/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)