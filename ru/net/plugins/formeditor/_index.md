---
title: Редактор Форм
type: docs
weight: 40
url: ru/net/plugins/formeditor/
description: Как добавить, обновить и удалить поля форм в файлах PDF с помощью плагинов Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

В этой статье мы покажем вам, как использовать [плагин Редактор Форм](https://products.aspose.org/pdf/net/form-editor/), который может добавлять, обновлять и удалять поля форм в файлах PDF.

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или новее
* Aspose.PDF для .NET 24.1 или новее
* Пример файла PDF, содержащего поля форм

Вы можете скачать библиотеку Aspose.PDF для .NET с официального сайта или установить ее с помощью NuGet Package Manager в Visual Studio.

## Шаги

Основные шаги для добавления, обновления и удаления полей форм в файлах PDF с использованием плагина FormEditor:

1. Создайте объект класса FormEditor
1. Создайте объект класса FormEditorAddOptions, FormEditorSetOptions или FormRemoveSelectedFieldsOptions, в зависимости от операции, которую вы хотите выполнить
1.
1. Запустите метод Process объекта FormEditor

Давайте посмотрим, как реализовать эти шаги на C# для каждой операции.

### Шаг 1: Создайте объект класса FormEditor

Класс FormEditor - это основной класс, который предоставляет функциональность добавления, обновления и удаления полей форм в файлах PDF. Чтобы использовать его, вам нужно создать экземпляр с помощью конструктора по умолчанию:

```cs
// Создание экземпляра плагина FormEditor
var plugin = new FormEditor();
```

### Шаг 2: Создайте объект класса FormEditorAddOptions, FormEditorSetOptions или FormRemoveSelectedFieldsOptions в зависимости от операции, которую вы хотите выполнить

Классы `FormEditorAddOptions`, `FormEditorSetOptions` и `FormRemoveSelectedFieldsOptions` являются вспомогательными классами, которые позволяют указывать различные параметры и настройки для операций редактирования форм, такие как типы полей форм, значения, свойства, предикаты и т.д.
Классы `FormEditorAddOptions`, `FormEditorSetOptions` и `FormRemoveSelectedFieldsOptions` являются вспомогательными классами, которые позволяют указывать различные опции и параметры для операций редактирования форм, такие как типы полей формы, значения, свойства, предикаты и т.д.

```cs
    // Создание опций для добавления полей формы.
    var options = new FormEditorAddOptions(
        [
            // Создать поле формы типа "флажок".
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // Создать поле формы типа "выпадающий список".
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // Создать текстовое поле формы.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
Чтобы обновить значения полей формы, чьи значения равны "a value" или "an another value" на "new value", вы можете использовать следующий код:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

Чтобы удалить поля формы, чья координата x нижнего левого угла больше 300, вы можете использовать следующий код:

```cs
// Создать опции для удаления полей формы
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Шаг 3: Добавьте источники входных и выходных данных в объект опций

Источниками входных и выходных данных являются PDF-файлы, которые вы хотите редактировать и сохранить.
Входные и выходные источники данных - это файлы PDF, которые вы хотите редактировать и сохранить.

```cs
// Укажите пути к входному и выходному файлам
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// Создайте новый экземпляр класса FileDataSource для входных и выходных файлов
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// Добавьте входные и выходные источники данных в параметры
options.AddInput(inputData);
options.AddOutput(outputData);
```

### Шаг 4: Запустите метод Process объекта FormEditor

Последний шаг - запустить метод Process объекта FormEditor, передав объект параметров в качестве параметра.
Последний шаг - запустить метод Process объекта FormEditor, передав объект options в качестве параметра.

```cs
// Обработать операцию редактирования формы с использованием плагина и опций
ResultContainer result = plugin.Process(options);

// Получить первый результат из коллекции результатов
var result = resultContainer.ResultCollection[0];

// Вывести результат
Console.WriteLine(result);
```

Результат будет содержать информацию, такую как пути к выходным файлам.
