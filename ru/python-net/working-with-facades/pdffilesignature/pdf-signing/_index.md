---
title: Подписать PDF документы
linktitle: Подписать PDF документы
type: docs
weight: 10
url: /ru/python-net/pdf-signing/
description: Узнайте, как подписывать PDF документы в Python с помощью PdfFileSignature, используя цифровые подписи, основанные на сертификате, именованные и видимые.
lastmod: "2026-04-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подписать PDF документы цифровыми подписями в Python
Abstract: В этой статье показано, как подписывать PDF документы с помощью Aspose.PDF for Python via .NET, используя фасад PdfFileSignature. Описывается настройка сертификата, подпись с базовыми параметрами, подпись с объектом PKCS7, назначение имени подписи и применение видимого оформления подписи.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для применения цифровых подписей к существующим PDF‑документам. Используя файл сертификата, вы можете подписать документ программно, разместить подпись на странице, назначить метаданные подписи и настроить отображение подписи.

В этой статье демонстрируются несколько типичных рабочих процессов подписи:

1. Создайте и привязать a `PdfFileSignature` объект во входном PDF.
1. Настройте сертификат подписи.
1. Примените цифровую подпись к целевой странице.
1. При необходимости задайте имя подписи и её видимый вид.
1. Сохраните подписанный PDF.

## Подготовьте переиспользуемые вспомогательные функции подписания

Прежде чем применять цифровую подпись к PDF, полезно создать небольшую группу переиспользуемых вспомогательных функций. Эти функции инициализируют обработчик подписи, определяют видимую область подписи, настраивают сертификат и создают переиспользуемые объекты подписи PKCS#7, чтобы примеры подписания ниже оставались автономными и их было проще понять.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## Подписание PDF с базовыми параметрами сертификата

Этот подход настраивает сертификат напрямую на `PdfFileSignature` объект. Это полезно, когда вам нужен простой процесс подписи со стандартными метаданными подписи и без отдельного управления объектом подписи.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Подписание PDF с объектом PKCS7

Использовать `PKCS7` объект, когда вам нужно сначала подготовить подпись, а затем передать её в вызов подписи. Этот шаблон даёт вам больший контроль над настройками подписи и является хорошей основой для более сложных рабочих процессов.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Подписание PDF с именованной подписью

Если ваш рабочий процесс с документом зависит от заранее определенного имени поля подписи, передайте это имя в `sign()`. Это упрощает последующее обращение к подписи для проверки, обработки или интеграции с процессом утверждения.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Применить видимую подпись

Вы можете сделать подпись видимой на странице PDF, присвоив ей пользовательский внешний вид `PKCS7` объекта. Это полезно, когда выходной документ должен отображать детали одобрения, такие как причина, место и контактная информация для конечных пользователей.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

