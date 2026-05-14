---
title: Ревизия и разрешения
linktitle: Ревизия и разрешения
type: docs
weight: 40
url: /ru/python-net/revision-permissions/
description: Узнайте, как проверять ревизии подписей, ревизии документов и разрешения на сертификацию в PDF‑файлах с помощью PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Чтение данных о ревизиях подписи PDF и разрешениях доступа в Python
Abstract: В этой статье объясняется, как проверять информацию о ревизиях и разрешениях в подписанных или сертифицированных PDF‑файлах с помощью Aspose.PDF for Python via .NET. Показано, как получить номер ревизии подписи, подсчитать общее количество ревизий документа и считывать разрешения доступа из сертифицированного PDF.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для работы с подписанными и заверенными PDF‑документами. Помимо добавления подписей, вы также можете просматривать метаданные подписи, чтобы понять, сколько ревизий содержит документ и какие изменения разрешены после сертификации.

В этом примере демонстрируются три типовых задачи инспекции:

1. Получить номер ревизии для существующей подписи.
1. Получить общее количество ревизий в подписанном документе.
1. Прочитать разрешения доступа из сертифицированного PDF.

## Получить номер ревизии подписи

Используйте этот подход, когда PDF уже содержит одну или несколько подписей, и вам необходимо определить ревизию, связанную с конкретной подписью. Пример получает имя первой доступной подписи и затем вызывает `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## Получить общее количество ревизий документа

Использовать `get_total_revision()` когда вам нужно узнать, сколько ревизий хранится в подписанном PDF. Это полезно для проверки того, прошёл ли документ через несколько обновлений после применения оригинальной подписи.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## Получить разрешения доступа из сертифицированного PDF

Сертифицированные документы могут определять, какие изменения разрешены после сертификации. Использовать `get_access_permissions()` проверить этот уровень разрешений и определить, разрешает ли документ отсутствие изменений, заполнение форм или другие контролируемые модификации.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```


