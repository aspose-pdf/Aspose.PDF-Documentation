---
title: Получить привилегии документа
linktitle: Получить привилегии документа
type: docs
weight: 10
url: /python-net/get-document-privileges/
description: Узнайте, как программно проверять привилегии PDF‑документа с помощью Aspose.PDF for Python. Этот учебный материал демонстрирует, как использовать класс PdfFileInfo для чтения настроек безопасности документа, таких как печать, копирование или изменение разрешений.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить привилегии PDF‑документа с помощью Aspose.PDF for Python
Abstract: PDF‑документы могут иметь ограничения безопасности, ограничивающие такие действия, как печать, копирование, изменение или заполнение форм. Получая эти привилегии программно, разработчики могут определить, какие операции разрешены для PDF. В этом руководстве показано, как использовать класс PdfFileInfo для получения привилегий документа PDF и их отображения в Python.
---

Привилегии PDF определяют, что пользователи могут и чего не могут делать с документом. Общие разрешения включают:

- Печать документа
- Копирование контента
- Изменение аннотаций или содержимого
- Заполнение полей формы
- Использование скринридеров
- Сборка или объединение документов

С помощью Aspose.PDF for Python вы можете программно проверять эти настройки, используя [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) класс. Это особенно полезно при работе с несколькими PDF в автоматизированных рабочих процессах, проверке соответствия или управлении обработкой документов в приложениях.

1. Загрузите PDF-файл.
1. Получите права доступа к документу.
1. Отобразите, какие действия разрешены для документа.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
