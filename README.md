# Tokyo Veg - A Guide to Vegetarian Restaurants in Tokyo

<div align=center>
<img src="https://github.com/user-attachments/assets/c6381bb3-1b8e-4e5f-aaa2-549c5ea06340" alt="TokyoVeg" width="155">

- Tokyo Veg 是一個基於 Django 的網站，旨在提供東京素食餐廳的資訊。 [[demo]](https://kageryo.pythonanywhere.com/)  
- 用戶可以瀏覽、搜尋和透過 [Issues](https://github.com/kageryo/tokyo_veg/issues) 提出加入新的素食餐廳。  

</div>

## 專案簡介

此專案使用 Django 3.2 開發，並儲存在 `food` app 中。
![image](https://github.com/user-attachments/assets/e240cdd1-ec8c-4386-800b-69f1de56d57d)

## 安裝與設定

以下是本專案的安裝與設定步驟：

1. **Clone 專案：**

    ```bash
    git clone https://github.com/kageryo/tokyo_veg.git
    cd tokyo_veg
    ```

2. **建立虛擬環境並啟動：**

    ```bash
    python3 -m venv tokyo_veg_venv
    source tokyo_veg_venv/bin/activate
    ```

3. **安裝函式庫：**

    ```bash
    pip install -r requirements.txt
    ```

4. **設置環境變數：**

    建立 `.env` 檔案並添加以下內容：

    ```plaintext
    SECRET_KEY=your-secret-key-here
    DEBUG=True（若您希望在正式環境中執行請勿開啟 DEBUG 以維護安全性）
    SENTRY_CLIENT_DSN = 'Your Sentry Key'
    ```

5. **遷移資料庫：**

    ```bash
    python manage.py migrate
    ```

6. **啟動開發伺服器：**

    ```bash
    python manage.py runserver
    ```

## 如何貢獻

我們歡迎各種形式的貢獻，包括但不限於：

- 報告 Bug
- 提出功能請求
- 撰寫或改進文件
- 提交 Pull Requests

### 提出 Issues

如果您有任何問題或功能請求，請透過 [Issues](https://github.com/kageryo/tokyo_veg/issues) 頁面提出。  
我們也歡迎用戶透過 [Issues](https://github.com/kageryo/tokyo_veg/issues) 提交新的餐廳資訊，請提供盡可能詳細的餐廳資料。

### 提交 Pull Requests

1. Fork 此專案。
2. 建立新的分支（`git checkout -b feature/YourFeature`）。
3. 提交您的修改（`git commit -m 'Add some feature'`）。
4. 將修改推送至分支（`git push origin feature/YourFeature`）。
5. 透過 GitHub 提交 Pull Request。

## 聯絡我們

如有任何問題，歡迎像我聯絡：[kageryo@coderyo.com](mailto:kageryo@codeyo.com)

### Reference
- [台南不需要米其林 TNFood](https://github.com/yen900611/TNFood/)
- [Heroku取消免費 試試PythonAnyWhere吧 | Django架站](https://www.hashimotodraw.com/article/5)

---

感謝您對 Tokyo Veg 的支持與貢獻！
