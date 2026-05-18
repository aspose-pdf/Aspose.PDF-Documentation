---
title: Системные требования
linktitle: Системные требования
type: docs
weight: 30
url: /ru/python-net/system-requirements/
description: В этом разделе перечислены поддерживаемые операционные системы, необходимые разработчику для успешной работы с Aspose.PDF for Python.
lastmod: "2025-02-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поддерживаемые операционные системы Aspose.PDF for Python через .NET
Abstract: > Aspose.PDF for Python via .NET — это API для обработки PDF, разработанное для разработчиков, позволяющее управлять PDF‑документами без необходимости использования Microsoft Office или Adobe Acrobat Automation. Оно поддерживает создание 32‑битных и 64‑битных Python‑приложений на различных операционных системах, включая Windows и Linux, где установлен Python 3.5 или более новая версия. API совместим с несколькими версиями Windows, от Windows XP до Windows 11, а также с основными дистрибутивами Linux, такими как Ubuntu, OpenSUSE и CentOS. Для систем Linux требуются специфические компоненты: библиотеки среды выполнения GCC‑6, зависимости .NET Core Runtime (без необходимости установки самого runtime) и сборка Python с pymalloc для версий 3.5‑3.7. Кроме того, необходима общая библиотека libpython, для которой может потребоваться настройка параметров, чтобы правильно распознавался путь к библиотеке.
---

## Обзор

Aspose.PDF for Python via .NET, API обработки PDF, позволяющий разработчикам работать с PDF‑документами без необходимости использовать Microsoft Office® или автоматизацию Adobe Acrobat. Aspose.PDF for Python может использоваться для создания 32‑разрядных и 64‑разрядных Python‑приложений для различных операционных систем (например, Windows и Linux), где установлен Python версии 3.5 или новее.

## Поддерживаемая операционная система

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- и другие

## Системные требования для целевого Linux

- Библиотеки выполнения GCC-6 (или более поздние).

- Зависимости .NET Core Runtime. Установка самого .NET Core Runtime НЕ требуется.

- Для Python 3.5-3.7: требуется сборка Python с pymalloc. Параметр сборки Python --with-pymalloc включён по умолчанию. Как правило, сборка Python с pymalloc отмечена суффиксом m в имени файла.

- Разделяемая библиотека libpython. Параметр сборки Python --enable-shared отключён по умолчанию, некоторые дистрибутивы Python не включают разделяемую библиотеку libpython. На некоторых платформах Linux разделяемую библиотеку libpython можно установить с помощью менеджера пакетов, например: sudo apt-get install libpython3.7. Распространённая проблема заключается в том, что библиотека libpython устанавливается в другое место, отличающееся от стандартного системного расположения разделяемых библиотек. Проблему можно решить, используя параметры сборки Python для указания альтернативных путей к библиотекам при компиляции Python, либо создав символическую ссылку на файл библиотеки libpython в стандартном системном расположении разделяемых библиотек. Обычно имя файла разделяемой библиотеки libpython имеет вид libpythonX.Ym.so.1.0 для Python 3.5‑3.7, или libpythonX.Y.so.1.0 для Python 3.8 и новее (например: libpython3.7m.so.1.0, libpython3.9.so.1.0).


