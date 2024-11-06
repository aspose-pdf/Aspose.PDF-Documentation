---

title: SharePointで安全なPDFを作成する

linktitle: 安全なPDFの作成

type: docs

weight: 60

url: ja/sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: PDF SharePoint APIを使用して、安全で暗号化されたPDFを作成し、SharePointでそのパスワードを指定できます。

---



{{% alert color="primary" %}}



Aspose.PDF for SharePointは、安全なPDFの作成をサポートしています。Aspose.PDF for SharePointをインストールすると、サイト設定に**PDF Secure Settings**オプションが追加されます。ここで、ユーザーパスワード、オーナーパスワード、アルゴリズムリストから任意の値を設定して、出力PDFを暗号化することができます。アルゴリズムリストは、異なる暗号化アルゴリズムとキーサイズの組み合わせを提供します。あなたの選んだ値を入力してください。



この記事では、Aspose.PDF for SharePointを使用して暗号化されたPDFを生成する方法を示します。



{{% /alert %}}



## **安全なPDFの作成**



この機能を示すために、まずオーナーおよびユーザーパスワードと暗号化アルゴリズムのための**PDF Secure Setting**オプションを設定します。 ドキュメントライブラリから2つのドキュメントをマージします。



### **PDFセキュリティ設定オプションの設定**



サイト設定から**PDFセキュリティ設定**オプションを開き、アルゴリズム、オーナーパスワード、ユーザーパスワードを設定します。



PDFファイルを暗号化する際に、異なるユーザーおよびオーナーパスワードを指定します。



- ユーザーパスワードが設定されている場合、それを入力しないとPDFを開くことができません。Acrobat Readerはユーザーにユーザーパスワードの入力を促します。間違っている場合、ドキュメントは開きません。

- オーナーパスワードが設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat Readerは権限設定に基づいてこれらの機能を禁止します。権限を設定/変更したい場合にはこのパスワードが必要です。



![todo:image_alt_text](creating-a-secure-pdf_1.png)



### **ドキュメントのマージ**



**PDFに変換**オプションを使用して2つのドキュメントをマージします。この機能は複数の非PDFファイル（HTML、テキストまたは画像）をPDFファイルにマージします。



1. Open a document library and select desired documents from the list.

ドキュメントライブラリを開き、リストから目的のドキュメントを選択します。

![todo:image_alt_text](creating-a-secure-pdf_2.png)

1. Use the **Merge to PDF** option from Library Tools to save the output file. You are prompted to save output file to disk.

ライブラリツールから**PDFにマージ**オプションを使用して出力ファイルを保存します。出力ファイルをディスクに保存するように求められます。

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Output**

出力ファイルは暗号化されています。

![todo:image_alt_text](creating-a-secure-pdf_4.png)