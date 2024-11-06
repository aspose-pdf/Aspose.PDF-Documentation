---
title: Создание сложного PDF с использованием Aspose.PDF
linktitle: Создание сложного PDF
type: docs
weight: 30
url: ru/androidjava/complex-pdf-example/
description: Aspose.PDF для Android через Java позволяет создавать более сложные документы, содержащие изображения, текстовые фрагменты и таблицы в одном документе.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Пример [Hello, World](/pdf/java/hello-world-example/) показал простые шаги по созданию PDF-документа с использованием Java и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с Java и Aspose.PDF для Java. В качестве примера возьмем документ от вымышленной компании, которая осуществляет пассажирские паромные перевозки.
Наш документ будет содержать изображение, два текстовых фрагмента (заголовок и абзац) и таблицу. Для создания такого документа мы будем использовать подход на основе DOM. Подробнее вы можете прочитать в разделе [Основы DOM API](/pdf/java/basics-of-dom-api/).

Если мы создаем документ с нуля, нам нужно следовать определенным шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). На этом этапе мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) к объекту документа. Теперь наш документ будет иметь одну страницу.
1. Чтобы добавить изображение, создайте FileInputStream, укажите путь к нужному нам файлу. Затем добавьте изображение в прямоугольник с заданными координатами.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) для заголовка. Для заголовка мы будем использовать шрифт Arial с размером 24pt и выравниванием по центру.
1. Добавьте заголовок в [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) страницы.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) для описания. Для описания мы будем использовать шрифт Arial с размером 24pt и выравниванием по центру.

1. Добавьте (описание) в абзацы страницы. Мы использовали шрифты "Helvetica" и "Times Roman" в нашем примере, но имейте в виду, что в Android всего три системных шрифта:

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. Создайте таблицу, добавьте свойства таблицы.
1. Добавьте (таблицу) на страницу [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Сохраните документ "Complex.pdf".

В конце отображается всплывающее окно с сообщением "PDF документ был создан!".

![Сложный пример Aspose.PDF для Android через Java](complex_example.png)

```java
package com.aspose.pdf.examplecomplex;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.Toast;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Cell;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.Page;
import com.aspose.pdf.Position;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.Row;
import com.aspose.pdf.Table;
import com.aspose.pdf.TextFragment;

import java.io.File;
import java.io.FileInputStream;
import java.time.Duration;
import java.time.LocalTime;

public class MainActivity extends AppCompatActivity {

    Button generate_button;
    File myExternalFile;
    String filepath;
    String filename;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        generate_button = (Button) findViewById(R.id.button);
        generate_button.setOnClickListener(v->RunComplexExample());

        if(!isExternalStorageAvailable()||isExternalStorageReadOnly()){
            generate_button.setEnabled(false);
        }
        else{
            filepath = "MyFileStorage";
            filename = "SampleFile.pdf";
            myExternalFile=new File(getExternalFilesDir(filepath), filename);
        }

    }

    private void RunComplexExample() {
        // Инициализировать объект документа
        Document document = new Document();

        // Добавить страницу
        Page page = document.getPages().add();

        // Добавить изображение
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Добавить изображение на страницу
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // Добавить заголовок
        TextFragment header = new TextFragment("Новые маршруты паромов осенью 2020");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Добавить описание
        String descriptionText = "Посетители должны покупать билеты онлайн, и билеты " +
                "ограничены до 5000 в день. Паромное обслуживание работает на половину " +
                "вместимости и по сокращенному расписанию. Ожидайте очереди.";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Добавить таблицу
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Отправление из города");
        headerRow.getCells().add("Отправление с острова");


        for (Cell headerRowCell : (Iterable<? extends Cell>) headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState()
                    .setForegroundColor(Color.getWhiteSmoke().toRgb());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/sample.pdf");

        Toast toast = Toast.makeText(MainActivity.this,
                "PDF документ был создан!", Toast.LENGTH_LONG);
        toast.show();
    }

    private static boolean isExternalStorageReadOnly(){
        String extStorageState= Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable(){
        String extStorageState=Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }

}
```


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/title"
        android:textSize="24sp"
        android:visibility="visible"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="64dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/generate_btn" />

</LinearLayout>
```