---
title: System Requirements
linktitle: System Requirements
type: docs
weight: 30
url: ru/python-net/system-requirements/
description: Этот раздел перечисляет поддерживаемые операционные системы, которые необходимы разработчику для успешной работы с Aspose.PDF для Python.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Overview

Aspose.PDF для Python через .NET, API для обработки PDF, который позволяет разработчикам работать с PDF-документами без необходимости в Microsoft Office® или Adobe Acrobat Automation. Aspose.PDF для Python можно использовать для разработки 32-битных и 64-битных приложений на Python для различных операционных систем (таких как Windows и Linux), на которых установлена версия Python 3.5 или выше.

## Supported Operating System

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


## System Requirements for Target Linux

- Библиотеки времени выполнения GCC-6 (или более поздние).

- Зависимости среды выполнения .NET Core. Установка самой среды выполнения .NET Core НЕ требуется.

- Для Python 3.5-3.7: Необходим сборка pymalloc для Python. Опция сборки Python --with-pymalloc включена по умолчанию. Обычно сборка pymalloc для Python обозначается суффиксом m в названии файла.

- Общая библиотека Python libpython.
 The --enable-shared Python build option is disabled by default, some Python distributions do not contain the libpython shared library. For some linux platforms, the libpython shared library can be installed using the package manager, for example: sudo apt-get install libpython3.7. The common issue is that libpython library is installed in a different location than the standard system location for shared libraries. The issue can be fixed by using the Python build options to set alternate library paths when compiling Python, or fixed by creating a symbolic link to the libpython library file in the system standard location for shared libraries. Typically, the libpython shared library file name is libpythonX.Ym.so.1.0 for Python 3.5-3.7, or libpythonX.Y.so.1.0 for Python 3.8 or later (for example: libpython3.7m.so.1.0, libpython3.9.so.1.0).



Опция сборки Python --enable-shared отключена по умолчанию, некоторые дистрибутивы Python не содержат общую библиотеку libpython. Для некоторых платформ Linux общая библиотека libpython может быть установлена с помощью менеджера пакетов, например: sudo apt-get install libpython3.7. Распространенной проблемой является то, что библиотека libpython установлена в другом месте, чем стандартное системное расположение для общих библиотек. Проблема может быть решена с помощью параметров сборки Python для установки альтернативных путей к библиотекам при компиляции Python или решена путем создания символической ссылки на файл библиотеки libpython в стандартном системном расположении для общих библиотек. Как правило, имя файла общей библиотеки libpython — libpythonX.Ym.so.1.0 для Python 3.5-3.7, или libpythonX.Y.so.1.0 для Python 3.8 или более поздних версий (например: libpython3.7m.so.1.0, libpython3.9.so.1.0).