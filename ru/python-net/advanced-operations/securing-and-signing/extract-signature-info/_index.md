---
title: Извлечь информацию о подписи из PDF на Python
linktitle: Извлечь детали из подписи
type: docs
weight: 20
url: /python-net/extract-image-and-signature-information/
description: Узнайте, как извлекать изображения подписей, сертификаты и детали цифровой подписи из PDF‑файлов в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Извлекайте изображения подписей и детали сертификатов из PDF‑файлов в Python.
Abstract: В этой статье объясняется, как извлекать изображения и информацию о цифровой подписи из PDF‑документов с помощью Aspose.PDF for Python. Узнайте, как получать изображения подписи, извлекать данные сертификата, проверять алгоритмы подписи и обнаруживать компрометированные подписи в подписанных PDF‑файлах.
---

## Извлечение изображения из поля подписи

Aspose.PDF for Python via .NET поддерживает возможность цифровой подписи PDF‑файлов с использованием [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) класс.

Используйте эти примеры, когда вам нужно просматривать подписанные PDF‑документы, экспортировать визуальные подписи или проверять целостность подписи в процессах проверки.

Этот фрагмент кода демонстрирует, как извлечь изображения цифровой подписи из PDF‑документа с помощью Aspose.PDF for Python.

Шаги:

1. Открытие PDF‑документа.
1. Перебор полей формы для поиска объектов SignatureField.
1. Извлечение изображения, связанного с каждой подписью (если доступно).
1. Сохранение извлечённого изображения подписи в файл JPEG.

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

## Извлечь информацию о подписи

Aspose.PDF for Python via .NET поддерживает возможность цифровой подписи PDF‑файлов с использованием класса SignatureField. В настоящее время мы также можем определить действительность сертификата, но не можем извлечь весь сертификат. Извлекаемая информация включает открытый ключ, отпечаток, издателя и т.д.

Чтобы извлечь информацию о подписи, мы ввели [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) метод к [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) класс. Пожалуйста, посмотрите на следующий фрагмент кода, который демонстрирует шаги по извлечению сертификата из объекта SignatureField:

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

## Извлечь цифровой сертификат из подписанного PDF

Извлеките цифровой сертификат, встроенный в подписанный PDF‑документ, с помощью Python и Aspose.PDF. Он сканирует поля подписи, извлекает поток сертификата и сохраняет его как отдельный файл для проверки или внешнего использования.

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

## Извлечь сертификаты подписи из PDF

Извлекать цифровые сертификаты из полей подписи PDF с использованием фасада PdfFileSignature в Python с Aspose.PDF. Он проходит по всем цифровым подписьям в документе и пытается получить вложенные сертификаты, подтверждая успешное извлечение.

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

## Извлечь внешние цифровые подписи

Внешние цифровые подписи в PDF‑документе. Проверяются все поля подписи в документе и подтверждается их подлинность, чтобы гарантировать, что файл не был изменён после подписания.

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

## Проверка подписей на компрометацию

Этот фрагмент кода демонстрирует, как обнаружить компрометированные цифровые подписи в PDF‑документе с использованием Aspose.PDF for Python.

Шаги включают:

1. Открытие PDF‑документа.
1. Создание экземпляра 'SignaturesCompromiseDetector' для анализа документа.
1. Проверка на наличие компрометированных (недействительных или изменённых) цифровых подписей.
1. Вывод имен всех найденных компрометированных подписей.
1. Отчет о покрытии подписью — указывающий, какая часть документа защищена действительными подписями.

Эта функция критически важна в сценариях, где необходимо проверять подлинность и целостность документа, таких как юридические, финансовые и регулируемые отрасли. Она позволяет разработчикам автоматически обнаруживать попытки подделки или повреждения подписанных PDF.

Aspose.PDF предлагает комплексный набор инструментов для проверки цифровой подписи, упрощая создание безопасных, учитывающих подписи приложений, которые поддерживают доверие к документам.

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

- [Обеспечьте безопасность и подпишите PDF‑файлы с помощью Python](/pdf/ru/python-net/securing-and-signing/)
- [Цифровая подпись PDF файлов в Python](/pdf/ru/python-net/digitally-sign-pdf-file/)
- [Подписать PDF‑документы со смарт‑карты в Python](/pdf/ru/python-net/sign-pdf-document-from-smart-card/)
- [Шифрование и расшифровка PDF‑файлов в Python](/pdf/ru/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
