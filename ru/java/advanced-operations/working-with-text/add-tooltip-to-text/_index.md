---
title: Использование всплывающей подсказки
linktitle: PDF Всплывающая подсказка
type: docs
weight: 20
url: ru/java/pdf-tooltip/
description: Узнайте, как добавить всплывающую подсказку к фрагменту текста в PDF с использованием Java и Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление всплывающей подсказки к найденному тексту путем добавления невидимой кнопки

Часто требуется добавить некоторые детали для фразы или конкретного слова в виде всплывающей подсказки в PDF-документ, чтобы она могла появиться, когда пользователь наводит курсор мыши на текст. Aspose.PDF для Java предоставляет эту возможность создания всплывающих подсказок, добавляя невидимую кнопку над найденным текстом. Следующий пример кода покажет вам, как достичь этой функциональности:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // Создать пример документа с текстом
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Наведите курсор мыши сюда, чтобы отобразить всплывающую подсказку"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("Наведите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку"));
        doc.save(outputFile);

        // Открыть документ с текстом
        Document document = new Document(outputFile);
        // Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Наведите курсор мыши сюда, чтобы отобразить всплывающую подсказку");
        // Применить абсорбер для страниц документа
        document.getPages().accept(absorber);
        // Получить извлеченные текстовые фрагменты
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // Пройти по фрагментам
        for(TextFragment fragment : textFragments)
        {
            // Создать невидимую кнопку на позиции текстового фрагмента
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Значение AlternateName будет отображаться в качестве всплывающей подсказки приложением просмотра
            field.setAlternateName ("Всплывающая подсказка для текста.");
            // Добавить кнопку в документ
            document.getForm().add(field);
        }

        // Далее будет пример очень длинной всплывающей подсказки
        absorber = new TextFragmentAbsorber("Наведите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Установить очень длинный текст
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // Сохранить документ
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

Что касается длины всплывающей подсказки, текст всплывающей подсказки содержится в PDF-документе как строка типа PDF, вне потока содержимого. В PDF-файлах нет эффективных ограничений на такие строки (см. PDF Reference Appendix C.). Однако соответствующий просмотрщик (например, Adobe Acrobat), работающий на определенном процессоре и в определенной операционной среде, имеет такие ограничения. Пожалуйста, обратитесь к документации приложения вашего PDF-просмотрщика.

{{% /alert %}}

## Создание скрытого текстового блока и его отображение при наведении мыши

В Aspose.PDF реализована функция скрытия действий, с помощью которой можно показывать/скрывать текстовое поле (или любой другой тип аннотации) при наведении/уходе мыши над некоторой невидимой кнопкой. Для этой цели используется класс Aspose.Pdf.Annotations.HideAction, чтобы назначить действие скрытия/показа текстовому блоку. Пожалуйста, используйте следующий фрагмент кода для показа/скрытия текстового блока при наведении/уходе мыши.

Пожалуйста, также учитывайте, что действия PDF в документах работают корректно в соответствующих просмотрщиках (например,
 Adobe Reader), но нет гарантий для других программ для чтения PDF (например, веб-браузерных плагинов). Мы провели краткое исследование и обнаружили:

- Все реализации действия скрытия в PDF-документах работают нормально в Internet Explorer v.11.0.
- Все реализации действия скрытия также работают в Opera v.12.14, но мы заметили задержку отклика при первом открытии документа.
- Только реализация с использованием конструктора HideAction, принимающего имя поля, работает, если документ открывается в Google Chrome v.61.0; Пожалуйста, используйте соответствующие конструкторы, если просмотр в Google Chrome имеет значение:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // Создаем пример документа с текстом
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Переместите указатель мыши сюда, чтобы отобразить всплывающий текст"));
        doc.save(outputFile);

        // Открыть документ с текстом
        Document document = new Document(outputFile);
        // Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Переместите указатель мыши сюда, чтобы отобразить всплывающий текст");
        // Применить абсорбер для страниц документа
        document.getPages().accept(absorber);
        // Получить первый извлеченный фрагмент текста
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // Создать скрытое текстовое поле для всплывающего текста в заданном прямоугольнике страницы
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // Установить текст, который будет отображаться в качестве значения поля
        floatingField.setValue ("Это \"всплывающее текстовое поле\".");
        // Мы рекомендуем сделать поле 'только для чтения' для этого сценария
        floatingField.setReadOnly(true);

        // Установить флаг 'hidden', чтобы сделать поле невидимым при открытии документа
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // Установка уникального имени поля не обязательна, но допустима
        floatingField.setPartialName ("FloatingField_1");

        // Установка характеристик внешнего вида поля не обязательна, но делает его лучше
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // Добавить текстовое поле в документ
        document.getForm().add(floatingField);

        // Создать невидимую кнопку на позиции текстового фрагмента
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // Создать новое действие скрытия для указанного поля (аннотации) и флага невидимости.
        // (Вы также можете ссылаться на всплывающее поле по имени, если вы его указали выше.)
        // Добавить действия при входе/выходе мыши на невидимое поле кнопки
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // Добавить поле кнопки в документ
        document.getForm().add(buttonField);

        // Сохранить документ
        document.save(outputFile);
    }
```