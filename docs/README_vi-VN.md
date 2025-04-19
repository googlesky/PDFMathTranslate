<div align="center">

[English](../README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [日本語](README_ja-JP.md) | [한국어](README_ko-KR.md) | Tiếng Việt

<img src="./images/banner.png" width="320px"  alt="PDF2ZH"/>  

<h2 id="title">PDFMathTranslate</h2>

<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pdf2zh/">
    <img src="https://img.shields.io/pypi/v/pdf2zh"/></a>
  <a href="https://pepy.tech/projects/pdf2zh">
    <img src="https://static.pepy.tech/badge/pdf2zh"></a>
  <a href="https://hub.docker.com/repository/docker/byaidu/pdf2zh">
    <img src="https://img.shields.io/docker/pulls/byaidu/pdf2zh"></a>
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Byaidu/PDFMathTranslate"/></a>
  <a href="https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97-Online%20Demo-FF9E0D"/></a>
  <a href="https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate">
    <img src="https://img.shields.io/badge/ModelScope-Demo-blue"></a>
  <a href="https://github.com/Byaidu/PDFMathTranslate/pulls">
    <img src="https://img.shields.io/badge/contributions-welcome-green"/></a>
  <a href="https://gitcode.com/Byaidu/PDFMathTranslate/overview">
    <img src="https://gitcode.com/Byaidu/PDFMathTranslate/star/badge.svg"></a>
  <a href="https://t.me/+Z9_SgnxmsmA5NzBl">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white"/></a>
</p>

<a href="https://trendshift.io/repositories/12424" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12424" alt="Byaidu%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

Công cụ dịch và đối chiếu song ngữ tài liệu PDF khoa học

- 📊 Giữ nguyên công thức, biểu đồ, mục lục và chú thích *([xem trước](#preview))*
- 🌐 Hỗ trợ [nhiều ngôn ngữ](./ADVANCED.md#language) và [đa dạng dịch vụ dịch thuật](./ADVANCED.md#services)
- 🤖 Cung cấp [công cụ dòng lệnh](#usage), [giao diện người dùng tương tác](#gui) và [Docker](#docker)

Hãy cung cấp phản hồi trong [GitHub Issues](https://github.com/Byaidu/PDFMathTranslate/issues) hoặc [Nhóm Telegram](https://t.me/+Z9_SgnxmsmA5NzBl).

Để biết chi tiết về cách đóng góp, vui lòng tham khảo [Hướng dẫn đóng góp](https://github.com/Byaidu/PDFMathTranslate/wiki/Contribution-Guide---%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97).

<h2 id="updates">Cập nhật</h2>

- [3 tháng 3, 2025] Hỗ trợ thử nghiệm cho backend mới [BabelDOC](https://github.com/funstory-ai/BabelDOC) WebUI được thêm vào như một tùy chọn thử nghiệm (bởi [@awwaawwa](https://github.com/awwaawwa))
- [22 tháng 2, 2025] CI phát hành tốt hơn và tệp exe windows-amd64 được đóng gói cẩn thận (bởi [@awwaawwa](https://github.com/awwaawwa))
- [24 tháng 12, 2024] Trình dịch giờ đây hỗ trợ các mô hình cục bộ trên [Xinference](https://github.com/xorbitsai/inference) _(bởi [@imClumsyPanda](https://github.com/imClumsyPanda))_
- [19 tháng 12, 2024] Tài liệu không phải PDF/A hiện được hỗ trợ bằng cách sử dụng `-cp` _(bởi [@reycn](https://github.com/reycn))_
- [13 tháng 12, 2024] Hỗ trợ bổ sung cho backend _(bởi [@YadominJinta](https://github.com/YadominJinta))_
- [10 tháng 12, 2024] Trình dịch giờ đây hỗ trợ các mô hình OpenAI trên Azure _(bởi [@yidasanqian](https://github.com/yidasanqian))_

<h2 id="preview">Xem trước</h2>

<div align="center">
<img src="./images/preview.gif" width="80%"/>
</div>

<h2 id="demo">Dịch vụ Trực tuyến 🌟</h2>

Bạn có thể dùng thử ứng dụng của chúng tôi bằng cách sử dụng một trong các demo sau:

- [Dịch vụ miễn phí công cộng](https://pdf2zh.com/) trực tuyến không cần cài đặt _(khuyến nghị)_.
- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 1000 trang miễn phí mỗi tháng. _(khuyến nghị)_
- [Demo được lưu trữ trên HuggingFace](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker)
- [Demo được lưu trữ trên ModelScope](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate) không cần cài đặt.

Lưu ý rằng tài nguyên tính toán của demo có hạn, vì vậy vui lòng tránh lạm dụng chúng.

<h2 id="install">Cài đặt và Sử dụng</h2>

### Phương pháp

Đối với các trường hợp sử dụng khác nhau, chúng tôi cung cấp các phương pháp khác nhau để sử dụng chương trình của chúng tôi:

<details open>
  <summary>1. Cài đặt UV</summary>

1. Python đã được cài đặt (3.10 <= phiên bản <= 3.12)
2. Cài đặt gói của chúng tôi:

   ```bash
   pip install uv
   uv tool install --python 3.12 pdf2zh
   ```

3. Thực hiện dịch thuật, các tệp được tạo ra trong [thư mục làm việc hiện tại](https://chatgpt.com/share/6745ed36-9acc-800e-8a90-59204bd13444):

   ```bash
   pdf2zh document.pdf
   ```

</details>

<details>
  <summary>2. Windows exe</summary>

1. Tải xuống pdf2zh-version-win64.zip từ [trang phát hành](https://github.com/Byaidu/PDFMathTranslate/releases)

2. Giải nén và nhấp đúp vào `pdf2zh.exe` để chạy.

</details>

<details>
  <summary id="gui">3. Giao diện người dùng đồ họa</summary>
1. Python đã được cài đặt (3.10 <= phiên bản <= 3.12)
2. Cài đặt gói của chúng tôi:

```bash
pip install pdf2zh
```

3. Bắt đầu sử dụng trong trình duyệt:

   ```bash
   pdf2zh -i
   ```

4. Nếu trình duyệt của bạn không được khởi động tự động, hãy truy cập

   ```bash
   http://localhost:7860/
   ```

   <img src="./images/gui.gif" width="500"/>

Xem [tài liệu cho GUI](./README_GUI.md) để biết thêm chi tiết.

</details>

<details>
  <summary id="docker">4. Docker</summary>

1. Kéo và chạy:

   ```bash
   docker pull byaidu/pdf2zh
   docker run -d -p 7860:7860 byaidu/pdf2zh
   ```

2. Mở trong trình duyệt:

   ```
   http://localhost:7860/
   ```

Đối với triển khai docker trên dịch vụ đám mây:

<div>
<a href="https://www.heroku.com/deploy?template=https://github.com/Byaidu/PDFMathTranslate">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" height="26"></a>
<a href="https://render.com/deploy">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Koyeb" height="26"></a>
<a href="https://zeabur.com/templates/5FQIGX?referralCode=reycn">
  <img src="https://zeabur.com/button.svg" alt="Deploy on Zeabur" height="26"></a>
<a href="https://app.koyeb.com/deploy?type=git&builder=buildpack&repository=github.com/Byaidu/PDFMathTranslate&branch=main&name=pdf-math-translate">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb" height="26"></a>
</div>

</details>

<details>
  <summary>5. Plugin Zotero</summary>

Xem [Zotero PDF2zh](https://github.com/guaguastandup/zotero-pdf2zh) để biết thêm chi tiết.

</details>

<details>
  <summary>6. Dòng lệnh</summary>

1. Python đã được cài đặt (3.10 <= phiên bản <= 3.12)
2. Cài đặt gói của chúng tôi:

   ```bash
   pip install pdf2zh
   ```

3. Thực hiện dịch thuật, các tệp được tạo ra trong [thư mục làm việc hiện tại](https://chatgpt.com/share/6745ed36-9acc-800e-8a90-59204bd13444):

   ```bash
   pdf2zh document.pdf
   ```

</details>

> [!TIP]
>
> - Nếu bạn đang sử dụng Windows và không thể mở tệp sau khi tải xuống, vui lòng cài đặt [vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe) và thử lại.
>
> - Nếu bạn không thể truy cập Docker Hub, vui lòng thử image trên [GitHub Container Registry](https://github.com/Byaidu/PDFMathTranslate/pkgs/container/pdfmathtranslate).
> ```bash
> docker pull ghcr.io/byaidu/pdfmathtranslate
> docker run -d -p 7860:7860 ghcr.io/byaidu/pdfmathtranslate
> ```

### Không thể cài đặt?

Chương trình hiện tại cần một mô hình AI (`wybxc/DocLayout-YOLO-DocStructBench-onnx`) trước khi hoạt động và một số người dùng không thể tải xuống do sự cố mạng. Nếu bạn gặp vấn đề khi tải xuống mô hình này, chúng tôi cung cấp một giải pháp thay thế bằng cách sử dụng biến môi trường sau:

```shell
set HF_ENDPOINT=https://hf-mirror.com
```

Đối với người dùng PowerShell:

```shell
$env:HF_ENDPOINT = https://hf-mirror.com
```

Nếu giải pháp không hiệu quả với bạn hoặc bạn gặp các vấn đề khác, vui lòng tham khảo [câu hỏi thường gặp](https://github.com/Byaidu/PDFMathTranslate/wiki#-faq--%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98).

<h2 id="usage">Tùy chọn Nâng cao</h2>

Thực hiện lệnh dịch thuật trong dòng lệnh để tạo tài liệu đã dịch `example-mono.pdf` và tài liệu song ngữ `example-dual.pdf` trong thư mục làm việc hiện tại. Sử dụng Google làm dịch vụ dịch thuật mặc định. Nhiều dịch vụ dịch thuật được hỗ trợ có thể tìm thấy [TẠI ĐÂY](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#services).

<img src="./images/cmd.explained.png" width="580px"  alt="cmd"/>

Trong bảng dưới đây, chúng tôi liệt kê tất cả các tùy chọn nâng cao để tham khảo:

| Tùy chọn        | Chức năng                                                                                                    | Ví dụ                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| files           | Tệp cục bộ                                                                                                   | `pdf2zh ~/local.pdf`                            |
| links           | Tệp trực tuyến                                                                                               | `pdf2zh http://arxiv.org/paper.pdf`             |
| `-i`            | [Vào GUI](#gui)                                                                                              | `pdf2zh -i`                                     |
| `-p`            | [Dịch một phần tài liệu](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#partial)      | `pdf2zh example.pdf -p 1`                       |
| `-li`           | [Ngôn ngữ nguồn](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#languages)            | `pdf2zh example.pdf -li en`                     |
| `-lo`           | [Ngôn ngữ đích](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#languages)             | `pdf2zh example.pdf -lo zh`                     |
| `-s`            | [Dịch vụ dịch thuật](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#services)         | `pdf2zh example.pdf -s deepl`                   |
| `-t`            | [Đa luồng](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#threads)                    | `pdf2zh example.pdf -t 1`                       |
| `-o`            | Thư mục đầu ra                                                                                               | `pdf2zh example.pdf -o output`                  |
| `-f`, `-c`      | [Ngoại lệ](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#exceptions)                 | `pdf2zh example.pdf -f "(MS.*)"`                |
| `-cp`           | Chế độ tương thích                                                                                           | `pdf2zh example.pdf --compatible`               |
| `--skip-subset-fonts` | [Bỏ qua tập con phông chữ](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#font-subset) | `pdf2zh example.pdf --skip-subset-fonts`        |
| `--ignore-cache` | [Bỏ qua bộ nhớ đệm dịch](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#cache)         | `pdf2zh example.pdf --ignore-cache`             |
| `--share`       | Liên kết công khai                                                                                           | `pdf2zh -i --share`                             |
| `--authorized`  | [Ủy quyền](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#auth)                       | `pdf2zh -i --authorized users.txt [auth.html]`  |
| `--prompt`      | [Lời nhắc tùy chỉnh](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#prompt)           | `pdf2zh --prompt [prompt.txt]`                  |
| `--onnx`        | [Sử dụng mô hình DocLayout-YOLO ONNX tùy chỉnh]                                                               | `pdf2zh --onnx [onnx/model/path]`               |
| `--serverport`  | [Sử dụng cổng WebUI tùy chỉnh]                                                                                | `pdf2zh --serverport 7860`                      |
| `--dir`         | [Dịch hàng loạt]                                                                                             | `pdf2zh --dir /path/to/translate/`              |
| `--config`      | [Tệp cấu hình](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#cofig)                   | `pdf2zh --config /path/to/config/config.json`   |
| `--serverport`  | [Cổng máy chủ gradio tùy chỉnh]                                                                               | `pdf2zh --serverport 7860`                      |
| `--babeldoc`    | Sử dụng backend thử nghiệm [BabelDOC](https://funstory-ai.github.io/BabelDOC/) để dịch                        | `pdf2zh --babeldoc -s openai example.pdf`       |

Để biết giải thích chi tiết, vui lòng tham khảo tài liệu của chúng tôi về [Sử dụng Nâng cao](./ADVANCED.md) để có danh sách đầy đủ các tùy chọn.

<h2 id="downstream">Phát triển Thứ cấp (API)</h2>

API pdf2zh hiện tại tạm thời không được dùng nữa. API sẽ được cung cấp lại sau khi [pdf2zh 2.0](https://github.com/Byaidu/PDFMathTranslate/issues/586) được phát hành. Đối với người dùng cần truy cập lập trình, vui lòng sử dụng hàm `babeldoc.high_level.async_translate` của [BabelDOC](https://github.com/funstory-ai/BabelDOC).

API này tạm thời không được dùng nữa có nghĩa là: mã liên quan sẽ không bị xóa bỏ trong thời gian này, nhưng không có hỗ trợ kỹ thuật và không có sửa lỗi nào sẽ được thực hiện.

<!-- Đối với các ứng dụng phát triển tiếp theo, vui lòng tham khảo tài liệu của chúng tôi về [Chi tiết API](./APIS.md) để biết thêm thông tin:

- [Python API](./APIS.md#api-python), cách sử dụng chương trình trong các chương trình Python khác
- [HTTP API](./APIS.md#api-http), cách giao tiếp với máy chủ đã cài đặt chương trình này -->

<h2 id="todo">Các việc cần làm</h2>

- [ ] Phân tích bố cục với các mô hình dựa trên DocLayNet, [PaddleX](https://github.com/PaddlePaddle/PaddleX/blob/17cc27ac3842e7880ca4aad92358d3ef8555429a/paddlex/repo_apis/PaddleDetection_api/object_det/official_categories.py#L81), [PaperMage](https://github.com/allenai/papermage/blob/9cd4bb48cbedab45d0f7a455711438f1632abebe/README.md?plain=1#L102), [SAM2](https://github.com/facebookresearch/sam2)

- [ ] Sửa xoay trang, mục lục, định dạng danh sách

- [ ] Sửa công thức pixel trong các bài báo cũ

- [ ] Thử lại bất đồng bộ ngoại trừ KeyboardInterrupt

- [ ] Thuật toán Knuth–Plass cho các ngôn ngữ phương Tây

- [ ] Hỗ trợ các tệp không phải PDF/A

- [ ] Plugin của [Zotero](https://github.com/zotero/zotero) và [Obsidian](https://github.com/obsidianmd/obsidian-releases)

<h2 id="acknowledgement">Lời cảm ơn</h2>

- [Immersive Translation](https://immersivetranslate.com) tài trợ mã đổi thành viên Pro hàng tháng cho những người đóng góp tích cực cho dự án này, xem chi tiết tại: [CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- Backend mới: [BabelDOC](https://github.com/funstory-ai/BabelDOC)

- Hợp nhất tài liệu: [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- Phân tích tài liệu: [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- Trích xuất tài liệu: [MinerU](https://github.com/opendatalab/MinerU)

- Xem trước tài liệu: [Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- Dịch đa luồng: [MathTranslate](https://github.com/SUSYUSTC/MathTranslate)

- Phân tích bố cục: [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- Tiêu chuẩn tài liệu: [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- Phông chữ đa ngôn ngữ: [Go Noto Universal](https://github.com/satbyy/go-noto-universal)

<h2 id="contrib">Người đóng góp</h2>

<a href="https://github.com/Byaidu/PDFMathTranslate/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a>

![Alt](https://repobeats.axiom.co/api/embed/dfa7583da5332a11468d686fbd29b92320a6a869.svg "Repobeats analytics image")

<h2 id="star_hist">Lịch sử Star</h2>

<a href="https://star-history.com/#Byaidu/PDFMathTranslate&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Date" />
   <img alt="Biểu đồ Lịch sử Star" src="https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Date"/>
 </picture>
</a>