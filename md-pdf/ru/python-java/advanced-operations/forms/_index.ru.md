---
title: Работа с формами с использованием Python
linktitle: Формы в PDF документе
type: docs
weight: 60
url: /python-java/forms/
lastmod: "2023-05-19"
description: Этот раздел содержит статьи, относящиеся к работе с формами в PDF документах с использованием Python API.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Формы — это файлы с областями для выбора или заполнения информации пользователями с целью сбора и хранения данных.

AcroForms — это PDF файлы, содержащие поля формы. Данные могут быть введены в эти поля (вручную или через автоматизированный процесс) конечными пользователями или автором формы. Внутренне AcroForms представляют собой аннотации или поля, примененные к PDF документу.

В этом разделе описан быстрый и простой подход к программному заполнению PDF документа с использованием Aspose.PDF. Раздел также обсуждает, как можно использовать Aspose.PDF для Java для обнаружения и отображения полей, доступных в существующем PDF с AcroForms.

**Наша библиотека Aspose.PDF for Python via Java** позволяет вам успешно, быстро и легко работать с формами в PDF документах.

- **AcroForms** - создание формы, заполнение поля формы, извлечение данных из формы, изменение полей в вашем PDF с помощью Java библиотеки.
- **XFA Forms** - заполнение полей XFA, преобразование XFA, получение свойств полей XFA.

## Доступны следующие функции:

- экспорт/импорт fdf
- экспорт/импорт xfdf
- экспорт/импорт xml
- экспорт/установка XfaData
- заполнение полей
- упрощение полей
- определение допустимых значений кнопок переключения
- получение имен полей, флагов, типов, значений
- переименование полей

```python

from asposepdf import Api, Forms


# инициализация лицензии
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# пример заполнения поля

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```