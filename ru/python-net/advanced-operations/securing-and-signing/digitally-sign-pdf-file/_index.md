---
title: Добавить цифровую подпись или подписать PDF в Python
linktitle: Подписать PDF цифровой подписью
type: docs
weight: 10
url: /ru/python-net/digitally-sign-pdf-file/
description: Цифрово подписывайте PDF‑документы, проверяйте или валидируйте подписанные цифровой подписью PDF с помощью Python.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Цифрово подпишите PDF‑файлы с помощью Python
Abstract: В данном руководстве объясняется, как цифрово подписывать PDF‑документы с использованием Aspose.PDF для Python через .NET. Описывается процесс применения стандартных и продвинутых цифровых подписей, использование сертификатов (PFX и PKCS#12) и настройка внешнего вида и поведения подписи. Документация содержит примеры кода, демонстрирующие, как подписать существующие PDF, добавить метки времени и проверить валидность подписи. Это позволяет разработчикам обеспечить подлинность, целостность документов и соответствие стандартам цифровой подписи в их Python‑приложениях.
---

## Подписать PDF цифровыми подписями

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Отдельная подпись **PKCS#7 detached signature** добавляет цифровую подпись к документу, не встраивая содержимое в блок подписи.

Следующий пример подписывает PDF‑документ с использованием отдельной цифровой подписи PKCS#7, применяя подпись к первой странице в указанной прямоугольной области.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Этот фрагмент кода на Python проверяет цифровую подпись в PDF‑файле с помощью метода 'file_sign.verify_signature()'.

1. Создаёт экземпляр PdfFileSignature, позволяющий работать с подписями в PDF.
1. Получить список имён подписи `get_signature_names(True)`.
1. Проверяет первую подпись в списке `verify_signature` на соответствие указанному сертификату.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## Добавить метку времени к цифровой подписи

### Как цифрово подписать PDF с меткой времени

Aspose.PDF для Python поддерживает цифровую подпись PDF с помощью сервера меток времени или веб‑сервиса.

Для выполнения этого требования в пространство имён Aspose.PDF был добавлен класс [НастройкиМеткиВремени](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/). Пожалуйста, посмотрите следующий фрагмент кода, который получает метку времени и добавляет её в PDF‑документ:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## Подписание PDF‑документов с использованием ECDSA

Подписание PDF‑документов с использованием ECDSA (Эллиптический алгоритм цифровой подписи) подразумевает использование криптографии эллиптических кривых для генерации цифровых подписей.

Приведённый выше фрагмент кода демонстрирует, как применить отдельную цифровую подпись PKCS#7 к PDF‑документу с помощью Aspose.PDF для Python. Загрузив документ, настроив внешний вид подписи и параметры безопасности, а затем сохранив результат, этот пример показывает полный и надёжный процесс цифровой подписи PDF‑файлов.

Этот метод обеспечивает подлинность и целостность документа, внедряя надёжную проверяемую подпись на первой странице. Использование SHA-256 в качестве алгоритма хэширования соответствует современным криптографическим стандартам, а возможность управлять расположением подписи предоставляет гибкость для видимых отметок одобрения.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
