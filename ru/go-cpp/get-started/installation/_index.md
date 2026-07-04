---
title: Как установить Aspose.PDF for Go через C++
linktitle: Установка
type: docs
weight: 20
url: /ru/go-cpp/installation/
description: В этом разделе показано описание продукта и инструкции по самостоятельной установке Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Руководство по установке Aspose.PDF for Go
Abstract: Руководство по установке Aspose.PDF for Go via C++ предоставляет пошаговые инструкции по установке и настройке библиотеки для использования в проектах Go с интеграцией C++. Оно охватывает различные методы установки, включая ручную настройку и использование менеджеров пакетов, таких как NuGet. Руководство также описывает системные требования, зависимости и необходимые шаги конфигурации, чтобы обеспечить бесшовную интеграцию в среды разработки. Эта документация помогает разработчикам эффективно начать работу с созданием, чтением и обработкой PDF‑документов в Go via C++.
SoftwareApplication: go-cpp
---

## Установка

Этот пакет включает большой файл, который хранится в виде архива bzip2.

1. Добавьте пакет asposepdf в свой проект:

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. Сгенерировать большой файл:

- **macOS и linux**

1. Откройте терминал

2. Перечислите папки github.com/aspose-pdf в кэше Go‑модулей:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. Перейдите из текущей папки в папку конкретной версии пакета, полученного на предыдущем шаге:

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

Замените `@vx.x.x` фактической версией пакета.

4. Запустите go generate с привилегиями суперпользователя:

```sh
sudo go generate
```

- **Windows**

1. Откройте командную строку

2. Перечислите папки github.com/aspose-pdf в кэше Go‑модулей:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. Перейдите из текущей папки в папку конкретной версии пакета, полученного на предыдущем шаге:

```cmd
cd <specific version folder of the package>
```

4. Запустите go generate:

```cmd
go generate
```

5. Добавьте папку конкретной версии пакета в переменную среды %PATH%:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

Заменить `<specific version folder of the package>` с фактическим путём, полученным на шаге 2.

## Тестирование

Тест запускается из корневой папки пакета:

```sh
go test -v
```

## Быстрый старт

Все фрагменты кода находятся в [фрагмент](https://github.com/aspose-pdf/aspose-pdf-go-cpp).
