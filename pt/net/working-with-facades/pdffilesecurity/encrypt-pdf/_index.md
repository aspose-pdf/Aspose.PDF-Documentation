---
title: Encrypt PDF File
type: docs
weight: 10
url: pt/net/encrypt-pdf-file/
description: Este tópico explica como criptografar um arquivo PDF usando a classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Criptografar um documento PDF protege seu conteúdo contra acesso não autorizado de fora, especialmente durante o compartilhamento ou arquivamento de arquivos.

Documentos PDF confidenciais podem ser criptografados e protegidos por senha. Somente o usuário que conhece a senha poderá descriptografar, abrir e visualizar esses documentos.

Vamos dar uma olhada em como a criptografia de PDF funciona com a biblioteca Aspose.PDF.

## Criptografar Arquivo PDF usando Diferentes Tipos de Criptografia e Algoritmos

Para criptografar um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) e então chamar o método [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Você pode passar a senha do usuário, a senha do proprietário e privilégios para o método [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Você também precisa passar os valores de KeySize e Algorithm para este método.

Revise uma lista possível de tal [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm):

|**Nome do membro**|**Valor**|**Descrição**|
| :- | :- | :- |
|RC4x40|0|RC4 com comprimento de chave 40.|
|RC4x128|1|RC4 com comprimento de chave 128.|
|AESx128|2|AES com comprimento de chave 128.|
|AESx256|3|AES com comprimento de chave 256.|

O trecho de código a seguir mostra como criptografar um arquivo PDF.

```csharp
public static void EncryptPDFFile()
        {
            // Criar objeto PdfFileSecurity
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // Criptografar arquivo usando criptografia de 256 bits
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```