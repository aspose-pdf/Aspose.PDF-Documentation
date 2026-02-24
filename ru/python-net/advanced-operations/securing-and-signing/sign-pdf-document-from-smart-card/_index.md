---
title: Как добавить подпись со смарт-картой в PDF
linktitle: Подписание PDF с помощью смарт-карты
type: docs
weight: 30
url: /ru/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF для Python через .NET позволяет подписывать PDF-документы со смарт-карты, используя поле подписи.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подписать PDF-документы со смарт-карты с помощью Python
Abstract: В этом руководстве объясняется, как цифровым способом подписывать PDF-документы с использованием смарт-карты при помощи Aspose.PDF для Python через .NET. Показано, как получить доступ к сертификатам, хранящимся на аппаратных устройствах (например, USB-токенах или смарт-картах) через хранилище сертификатов Windows, и использовать их для подписи PDF‑файлов. Документация включает примеры кода, демонстрирующие, как найти нужный сертификат, настроить свойства подписи и встроить цифровую подпись в PDF. Это обеспечивает безопасную подпись, поддерживаемую аппаратным обеспечением, в соответствии со стандартами цифровой подписи, подходящую для высокодоверенных корпоративных и юридических процессов.
---

Aspose.PDF предоставляет мощные возможности для интеграции визуальных и криптографических компонентов подписи, обеспечивая подлинность и профессиональное оформление в цифрово подписанных PDF‑документах.

## Подписание со смарт-картой с использованием поля подписи

В этом примере показано, как цифровой подпись PDF‑документа с использованием внешнего сертификата при помощи Aspose.PDF для Python и применить пользовательское изображение внешнего вида подписи:

1. Открытие PDF‑документа.
1. Создание объекта PdfFileSignature и привязка его к документу.
1. Получение локального цифрового сертификата с помощью пользовательского метода `get_local_certificate()`.
1. Настройка ExternalSignature на основе выбранного сертификата.
1. Применение пользовательского изображения внешнего вида подписи (например, логотип компании или рукописная подпись).
1. Цифровая подпись первой страницы документа с указанными метаданными (причина, контакт, местоположение).
1. Сохранение подписанного документа в новый выходной файл.

Этот метод идеален для случаев, когда подписи необходимо применять программно с использованием внешних сертификатов — таких как аппаратные токены, хранилища сертификатов или доверенные провайдеры — и представлять их с персонализированным визуальным оформлением.

Ниже представлены фрагменты кода для подписи PDF‑документа со смарт-карты:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## Проверка цифровых подписей

Этот фрагмент кода демонстрирует, как проверить цифровые подписи в PDF‑документе с использованием Aspose.PDF для Python:

1. Открытие PDF‑файла.
1. Создание 'PdfFileSignature object' и привязка его к документу.
1. Получение списка всех имен полей подписи с помощью 'get_signature_names()'.
1. Итерация по каждой подписи и проверка её действительности с помощью 'verify_signature()'.
1. Генерация исключения, если проверка любой подписи не удалась.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## Подписание внешним сертификатом

Этот фрагмент кода демонстрирует, как добавить и подписать поле цифровой подписи в PDF‑документе с использованием Aspose.PDF для Python и внешнего сертификата:

1. Открытие PDF‑файла как бинарного потока.
1. Создание SignatureField и размещение его на первой странице документа в указанной позиции.
1. Получение локального цифрового сертификата с помощью пользовательского метода `get_local_certificate()`.
1. Настройка ExternalSignature с метаданными, такими как организация, причина и контактная информация.
1. Присвоение уникального имени полю подписи (partial_name = "sig1").
1. Добавление поля подписи в форму PDF.
1. Подписание поля внешним сертификатом.
1. Сохранение подписанного документа в выходной файл.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


