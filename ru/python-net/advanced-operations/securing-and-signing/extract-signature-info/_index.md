---
title: Извлечь детали из подписи
linktitle: Извлечь детали из подписи
type: docs
weight: 20
url: /ru/python-net/extract-image-and-signature-information/
description: Как извлечь изображение из цифровой подписи в PDF‑документах с помощью Aspose.PDF для Python.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить детали подписи в PDF с помощью Python
Abstract: В этой статье демонстрируется, как извлечь изображения и информацию о цифровой подписи из PDF‑документов с помощью Aspose.PDF для Python. Предоставлены пошаговые инструкции и образцы кода для идентификации, доступа и сохранения встроенных изображений, а также получения метаданных и статуса проверки цифровых подписей.
---

## Извлечение изображения из поля подписи

Aspose.PDF for Python via .NET поддерживает возможность цифровой подписи PDF‑файлов с использованием класса [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) .

Этот фрагмент кода демонстрирует, как извлекать изображения цифровой подписи из PDF‑документа с помощью Aspose.PDF for Python.

Шаги:

1. Открытие PDF‑документа.
1. Итерация по полям формы для поиска объектов SignatureField.
1. Извлечение изображения, связанного с каждой подписью (если доступно).
1. Сохранение извлечённого изображения подписи в файл JPEG.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## Извлечение информации о подписи

Aspose.PDF for Python via .NET поддерживает возможность цифровой подписи PDF‑файлов с использованием класса SignatureField. В настоящее время мы также можем определить валидность сертификата, но не можем извлечь весь сертификат. Доступная для извлечения информация включает открытый ключ, отпечаток, издателя и т.п.

Для извлечения информации о подписи мы добавили метод [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) в класс [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) . Пожалуйста, посмотрите следующий фрагмент кода, демонстрирующий шаги по извлечению сертификата из объекта SignatureField:

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

Вы можете получить информацию о алгоритмах подписи документа.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## Проверка подписи на компрометацию

Этот фрагмент кода демонстрирует, как обнаруживать компрометированные цифровые подписи в PDF‑документе с помощью Aspose.PDF for Python.

Шаги включают:

1. Открытие PDF‑документа.
1. Создание экземпляра 'SignaturesCompromiseDetector' для анализа документа.
1. Проверка наличия компрометированных (недействительных или изменённых) цифровых подписей.
1. Вывод имён найденных компрометированных подписей.
1. Сообщение о покрытии подписи — указывает, какая часть документа защищена действительными подписями.

Эта функция имеет критическое значение в сценариях, где необходимо проверять подлинность и целостность документа, таких как юридические, финансовые и регулируемые среды. Она позволяет разработчикам автоматически обнаруживать попытки подделки или повреждения подписанных PDF‑файлов.

Aspose.PDF предлагает полный набор инструментов для валидации цифровой подписи, упрощая создание безопасных приложений, учитывающих подписи, и поддерживая надёжность документов.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

