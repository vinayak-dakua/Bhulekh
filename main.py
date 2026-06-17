from playwright.sync_api import sync_playwright
import pyautogui

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    page = browser.new_page()

    print("1. Opening Bhulekh")

    page.goto(
        "https://bhulekh.ori.nic.in/RoRView.aspx"
    )

    print("2. URL =", page.url)

    # Error page handle
    if "BhulekhError.aspx" in page.url:

        print("3. Error page found")

        page.get_by_role(
            "link",
            name="here"
        ).click()

        page.wait_for_load_state("networkidle")

        print("4. New session opened")

    print("5. Selecting District")

    page.select_option(
        "#ctl00_ContentPlaceHolder1_ddlDistrict",
        label="ଗଂଜାମ"
    )

    page.wait_for_timeout(3000)

    print("6. District Done")

    page.select_option(
        "#ctl00_ContentPlaceHolder1_ddlTahsil",
        label="ହିଞ୍ଜିଳିକାଟୁ"
    )

    page.wait_for_timeout(3000)

    print("7. Tahasil Done")

    page.select_option(
        "#ctl00_ContentPlaceHolder1_ddlVillage",
        label="ନୂଆଗଡ଼"
    )

    page.wait_for_timeout(15000)

    print("8. Village Done")

    page.get_by_label("Plot").check()

    page.wait_for_timeout(10000)

    print("9. Plot Clicked")

    page.wait_for_selector(
        "#ctl00_ContentPlaceHolder1_ddlBindData"
    )

    page.wait_for_timeout(10000)

    print("10. Reading Dropdown")

    all_options = page.eval_on_selector_all(
        "#ctl00_ContentPlaceHolder1_ddlBindData option",
        "els => els.map(e => e.textContent)"
    )

    print("11. Options Loaded =", len(all_options))

    plots = [
        x.strip()
        for x in all_options
        if x and x.strip().startswith("775")
    ]

    print("12. 775 Plots Found =", len(plots))
    plots = list(dict.fromkeys(plots))

    print("Unique plots =", len(plots))

    for plot in plots:

        print(f"\nProcessing Plot: {plot}")

        try:

            # Plot select
            page.select_option(
                "#ctl00_ContentPlaceHolder1_ddlBindData",
                label=plot
            )

            page.wait_for_timeout(5000)

            # View RoR
            page.get_by_role(
                "button",
                name="View RoR"
            ).click()

            page.wait_for_timeout(5000)

            print("RoR Opened")

            # Bottom scroll
            page.evaluate(
                "window.scrollTo(0, document.body.scrollHeight)"
            )

            page.wait_for_timeout(5000)

            # Print click
            page.get_by_text(
                "Print",
                exact=True
            ).click()

            page.wait_for_timeout(5000)

            print("Print Dialog Opened")

            # Print button
            pyautogui.press("enter")

            page.wait_for_timeout(5000)

            # File name
            safe_name = (
                plot
                .replace("/", "_")
                .replace(" ", "")
            )

            pyautogui.write(
                f"{safe_name}.pdf"
            )

            page.wait_for_timeout(7000)

            # Save
            pyautogui.press("enter")

            page.wait_for_timeout(7000)

            print(f"PDF Saved: {safe_name}.pdf")

            # # PDF Viewer close
            # pyautogui.hotkey("alt", "f4")

            # page.wait_for_timeout(7000)

            # Print preview close
            pyautogui.hotkey("alt", "f4")

            page.wait_for_timeout(7000)

            print("Preview Closed")

            # Selection page par wapas
            page.goto(
                "https://bhulekh.ori.nic.in/RoRView.aspx"
            )

            page.wait_for_timeout(5000)

            # Error page handle
            if "BhulekhError.aspx" in page.url:

                page.get_by_role(
                    "link",
                    name="here"
                ).click()

                page.wait_for_load_state(
                    "networkidle"
                )

            # District
            page.select_option(
                "#ctl00_ContentPlaceHolder1_ddlDistrict",
                label="ଗଂଜାମ"
            )

            page.wait_for_timeout(3000)

            # Tahasil
            page.select_option(
                "#ctl00_ContentPlaceHolder1_ddlTahsil",
                label="ହିଞ୍ଜିଳିକାଟୁ"
            )

            page.wait_for_timeout(3000)

            # Village
            page.select_option(
                "#ctl00_ContentPlaceHolder1_ddlVillage",
                label="ନୂଆଗଡ଼"
            )

            page.wait_for_timeout(15000)

            # Plot
            page.get_by_label("Plot").check()

            page.wait_for_timeout(10000)

            print("Ready For Next Plot")

        except Exception as e:

            print(
                f"FAILED : {plot}",
                str(e)
            )

    print("\nALL PLOTS COMPLETED")

    browser.close()