---
title: Add Multimedia Annotation
type: docs
weight: 120
url: /net/add-multimedia-annotation/
---
# Add Multimedia Annotation

When you need to add an external video link in PDF document, you can use [MovieAnnotaiton](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation). However, when there is a requirement to embed media inside PDF document, you need to use [RichMediaAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

This annotation allows to embed media file within PDF document and set video/audio player, implemented as flash application. 

Due to license restriction, we can not include third-party flash scripts in our product, so you should provide your script for playing video or audio. You should provide a flash application code. For example, you can use videoplayer.swf and audioplayer.swf which are distributed with Adobe Acrobat and may be found in Multimedia Skins/Players subfolder in Acrobat folder. Another choice is using StrobeMediaPLayback.swf player or any other video player implemented in flash.

The following methods/properties of RichMediaAnnotation class can be used.

- Stream CustomPlayer { set; }: Allows setting player used to play video.
- string CustomFlashVariables { set; }: Allows to set variables that are passed to flash application. This line is set of “key=value” pairs which are separated with ‘&';
- void AddCustomData(strig name, Stream data):  Add additional data for the player. For example source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}:  Event activates player; possible values are Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Set video/audio data to be played
- void Update():  Create a data structure of the annotation. This method should be called last
- void SetPoster(Stream): Set poster of the video i.e. picture shown when the player is not active

## Embed Video File
A Movie Annotation contains animated graphics and sound to be presented on the computer screen and through the speakers.

Embedding video file can be achieved using the following sample code.

C#
```cshrap
 string myDir = "C:/Temp/";


Aspose.PDF.Document doc = new Aspose.PDF.Document();

Page page = doc.Pages.Add();

RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.PDF.Rectangle(100,500, 300, 600));

//here we should specify stream containing code of the video player

rma.CustomPlayer = new FileStream(@"C:\Adobe\Acrobat 11.0\Acrobat\MultimediaSkins\Players\Videoplayer.swf",FileMode.Open,FileAccess.Read);

//give name to video data. This data will be embedded into document with this name and referenced from flash variables by this name. 

//videoName should not contain path to the file; this is rather "key" to access data inside of the PDF document

string videoName = "VideoTutorial.mp4";

//also we use skin for video player

string skinName = "SkinOverAllNoFullNoCaption.swf";

//compose flash variables line for player. please note that different players may have different format of the flash variables line. Refer to documentation for your player.

rma.CustomFlashVariables = String.Format("source={0}&skin={1}", "VideoTutorial.mp4", skinName);

//add skin code. 

rma.AddCustomData(skinName,new FileStream(@"C:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\Multimedia Skins\SkinOverAllNoFullNoCaption.swf",FileMode.Open, FileAccess.Read));

//set poster for video

rma.SetPoster(new FileStream(myDir + "barcode.jpg",FileMode.Open, FileAccess.Read));

Stream fs = new FileStream(myDir + videoName, FileMode.Open, FileAccess.Read);

//set video content

rma.SetContent(videoName, fs);

//set type of the content (video)

rma.Type = RichMediaAnnotation.ContentType.Video;

//active player by click

rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

//update annotation data. This method should be called after all assignments/setup. This method initializes data structure of the annotation and embeds required data. 

rma.Update();

//add annotation on the page.

page.Annotations.Add(rma);

doc.Save(myDir + "Output.pdf");
```

## Embed Audio File
A Sound Annotation  shall analogous to a text annotation except that instead of a text note, it contains sound recorded from the computer’s microphone or imported from a file.

Embedding audio files can be achieved using the following sample code.

C#
```
 Aspose.PDF.Document

doc = new Aspose.PDF.Document();

Page page = doc.Pages.Add();

//give name to audio data. This data will be embedded into document with this name and referenced from flash variables by this name. 

string audioName = "test_cbr.mp3";

RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.PDF.Rectangle(100,650, 300, 670));

Stream fs = new FileStream(myDir+audioName, FileMode.Open, FileAccess.Read);

//here we should specify stream containing code of the audio player

rma.CustomPlayer = new FileStream(@"C:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\MultimediaSkins\Players\Audioplayer.swf", FileMode.Open,

FileAccess.Read);

//compose flash variables line for player. please note that different players may have different format of the flash variables line. Refer to documentation for your player.

rma.CustomFlashVariables = String.Format("source={0}", "test_cbr.mp3");

//active player on page open event

rma.ActivateOn = RichMediaAnnotation.ActivationEvent.PageOpen;

//set audio content

rma.SetContent(audioName, fs);

//set type of the content (audio)

rma.Type = RichMediaAnnotation.ContentType.Audio;

//update annotation data. This method should be called after all assignments/setup. This method initializes data structure of the annotation and embeds required data. 

rma.Update();

//add annotation on the page.

page.Annotations.Add(rma);

doc.Save(myDir+"39606-2.pdf");
```
