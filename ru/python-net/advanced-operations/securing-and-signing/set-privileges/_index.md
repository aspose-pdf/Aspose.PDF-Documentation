---
title: Установить привилегии, шифровать и расшифровывать PDF
linktitle: Шифрование и расшифровка PDF файла
type: docs
weight: 70
url: /ru/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Зашифровать PDF файл с помощью Python, используя различные типы шифрования и алгоритмы. Также расшифровывать PDF файлы с помощью пароля владельца.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Шифрование или расшифровка PDF файла с помощью Python
Abstract: Эта страница документации объясняет, как установить привилегии документа, применить шифрование и расшифровать PDF файлы с использованием Aspose.PDF для Python. Она помогает разработчикам настраивать пароли пользователя и владельца, определять ограничения доступа (например, печать, копирование или редактирование). Примеры кода показывают, как защищать конфиденциальный контент и эффективно управлять безопасностью PDF в приложениях на Python, обеспечивая контролируемый доступ и конфиденциальность данных.
---

Управление безопасностью документа является необходимым при работе с конфиденциальным или критически важным бизнес-контентом. Aspose.PDF для Python через .NET предоставляет мощный API для программного применения шифрования, контроля доступа через разрешения и расшифровки защищённых PDF файлов.

Эта статья проводит разработчиков Python через практические примеры установки привилегий, применения и снятия шифрования, изменения паролей и определения состояний защиты — всё в рамках рабочего процесса с PDF.

Aspose.PDF для Python через .NET даёт разработчикам полный контроль над безопасностью PDF:

**Set Privileges** - Тонко настроенный контроль доступа с использованием разрешений.
**Encrypt File** - Применить шифрование AES или RC4 с пользовательскими паролями.
**Decrypt File** - Снять защиту с помощью пароля владельца.
**Change Passwords** - Поменять или обновить учётные данные без изменения содержимого.
**Inspect Security** - Определять статус шифрования или требуемые типы паролей.

## Установить привилегии в существующем PDF файле

Вы можете ограничить или разрешить конкретные операции (например, печать, копирование, заполнение форм), задавая пароли пользователя и владельца вместе с правами доступа.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## Шифрование PDF файла с использованием разных типов шифрования и алгоритмов

Шифрование PDF гарантирует, что только пользователи с действительными учётными данными могут открыть или изменить файл.

>Ключевые термины:

- Пароль пользователя. Требуется для открытия документа.

- Пароль владельца. Требуется для изменения разрешений или снятия шифрования.

- Размер ключа. Используйте AE_SX128 для максимальной безопасности в современных рабочих процессах.

Следующий фрагмент кода показывает, как зашифровать PDF файлы.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## Расшифровка PDF файла с использованием пароля владельца

Для снятия защиты паролем и восстановления полного доступа:

1. Загружает зашифрованный PDF, используя правильный пароль ('password' — пароль пользователя или владельца).
1. Удаляет всю защиту паролем и настройки шифрования из документа.
1. Сохраняет теперь незащищённый PDF в указанный файл вывода.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## Смена пароля PDF файла

Для обновления учётных данных безопасности (паролей пользователя и владельца) PDF документа при сохранении его содержимого и структуры.

1. Открывает PDF, используя существующий пароль владельца ('owner'), который предоставляет полный доступ, включая возможность менять настройки безопасности.
1. Заменяет старые пароли новым паролем пользователя ('newuser') и новым паролем владельца ('newowner').
1. Сохраняет PDF с обновлёнными настройками пароля.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## Как определить, защищён ли исходный PDF паролем

### Определить правильный пароль из массива

В некоторых сценариях может потребоваться определить правильный пароль из списка потенциальных вариантов, чтобы получить доступ к защищённому PDF. Приведённый ниже фрагмент кода демонстрирует, как проверить, защищён ли PDF файл паролем, и попытаться открыть его, перебирая предопределённый список паролей с помощью Aspose.PDF для Python через .NET.

Процесс включает:

1. Использование PdfFileInfo для определения, зашифрован ли PDF.
1. Пытается открыть PDF с каждым паролем, используя ap.Document().
1. При успехе выводит количество страниц.
1. Если нет, ловит исключение и сообщает о неудачном пароле.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


