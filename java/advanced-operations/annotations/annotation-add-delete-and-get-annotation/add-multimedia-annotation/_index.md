---
title: PDF Multimedia Annotation 
linktitle: Multimedia Annotation
type: docs
weight: 120
url: /java/multimedia-annotation/
description: Aspose.PDF for Java allows you to add, get, and delete the multimedia annotation from your PDF document.
lastmod: "2021-01-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Annotations in a PDF document are contained in a [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) object’s Annotations collection. This collection contains all annotations for that individual page only: every page has its own Annotations collection. To add an annotation to a particular page, add it to that page’s Annotations collection using the Add method. 

Use the [ScreenAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) class in the Aspose.PDF.InteractiveFeatures.Annotations namespace to include SWF files as annotations in a PDF document instead. A screen annotation specifies a region of a page upon which media clips may be played.

When you need to add an external video link in PDF document, you can use [MovieAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation).
A Movie Annotation contains animated graphics and sound to be presented on the computer screen and through the speakers.

A [Sound Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) shall analogous to a text annotation except that instead of a text note, it contains sound recorded from the computer’s microphone or imported from a file. When the annotation is activated, the sound shall be played. The annotation shall behave like a text annotation in most ways, with a different icon (by default, a speaker) to indicate that it represents a sound. 

However, when there is a requirement to embed media inside PDF document, you need to use [RichMediaAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).

The following methods/properties of RichMediaAnnotation class can be used.

- Stream CustomPlayer { set; }: Allows setting player used to play video.
- string CustomFlashVariables { set; }: Allows to set variables that are passed to flash application. This line is set of “key=value” pairs which are separated with ‘&'.
- void AddCustomData(strig name, Stream data):  Add additional data for the player. For example source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}:  Event activates player; possible values are Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Set video/audio data to be playedю
- void Update():  Create a data structure of the annotation. This method should be called last
- void SetPoster(Stream): Set poster of the video i.e. picture shown when the player is not active

## Add Screen Annotation 

The following code snippet shows how to add Screen Annotation to a PDF file: 

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // Create Screen Annotation
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
```
## Add Sound Annotation 

The following code snippet shows how to add Sound Annotation to a PDF file: 

```java
          public static void AddSoundAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Sound Annotation demo");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```
## Add RichMediaAnnotation

The following code snippet shows how to add RichMediaAnnotation to a PDF file:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // give name to video data. This data will be embedded into document with this
        // name and referenced from flash variables by this name.
        // videoName should not contain path to the file; this is rather "key" to access
        // data inside of the PDF document

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // also we use skin for video player
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // here we should specify stream containing code of the video player
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // compose flash variables line for player. please note that different players
        // may have different format of the flash variables line.
        // Refer to documentation for your player.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // add skin code.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // set poster for video
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // set video content
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // set type of the content (video)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // active player by click
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // update annotation data. This method should be called after all
        // assignments/setup. This method initializes data structure of the annotation
        // and embeds required data.
        rma.update();

        // add annotation on the page.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```
## Get MultimediaAnnotation 

Please try using the following code snippet to Get MultimediaAnnotation from PDF document.

```java
public static void GetMultimediaAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }        
```
## Delete MultimediaAnnotation

The following code snippet shows how to Delete MultimediaAnnotation from PDF file.

```java
    public static void DeletePolyAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
}   
```
