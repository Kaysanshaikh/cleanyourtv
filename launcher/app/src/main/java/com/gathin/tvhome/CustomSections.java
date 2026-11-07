package com.gathin.tvhome;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Handler;
import android.os.Looper;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public final class CustomSections {

    public static final int ID_APPS_ROW = 10001;
    public static final int ID_FAV_ROW = 10002;
    public static final int ID_MOODS_ROW = 10003;
    public static final int ID_MORE_APPS = 10004;

    public static final class TitleItem {
        public final String title;
        public final String character;
        public final String app;
        public final String pkg;
        public final String url;
        public final int color;
        public final int appIconRes;
        public final int sceneRes;

        public TitleItem(String title, String character, String app, String pkg, String url, int color, int appIconRes) {
            this(title, character, app, pkg, url, color, appIconRes, 0);
        }

        public TitleItem(String title, String character, String app, String pkg, String url, int color, int appIconRes, int sceneRes) {
            this.title = title;
            this.character = character;
            this.app = app;
            this.pkg = pkg;
            this.url = url;
            this.color = color;
            this.appIconRes = appIconRes;
            this.sceneRes = sceneRes;
        }
    }

    public static final class Mood {
        public final String name;
        public final int color;
        public final int count;
        public final String suggestions;
        public final List<TitleItem> titles;

        public Mood(String name, int color, int count, String suggestions, List<TitleItem> titles) {
            this.name = name;
            this.color = color;
            this.count = count;
            this.suggestions = suggestions;
            this.titles = titles;
        }
    }

    public static final List<TitleItem> FAVOURITES = Arrays.asList(
        new TitleItem("The Mentalist", "Patrick Jane", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com/detail?gti=amzn1.dv.gti.mentalist", 0xFF4DABF7, R.drawable.ic_dock_prime, R.drawable.fav_mentalist),
        new TitleItem("The Big Bang Theory", "Sheldon Cooper", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70143830", 0xFFF2B84B, R.drawable.ic_dock_netflix, R.drawable.fav_sheldon),
        new TitleItem("Master", "JD", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com/detail?gti=amzn1.dv.gti.master", 0xFFFF922B, R.drawable.ic_dock_prime, R.drawable.fav_master),
        new TitleItem("Breaking Bad", "Walter White", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70143836", 0xFF20C997, R.drawable.ic_dock_netflix, R.drawable.fav_walter),
        new TitleItem("The Flash", "Reverse-Flash", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/80027042", 0xFFFFD43B, R.drawable.ic_dock_netflix, R.drawable.fav_flash),
        new TitleItem("Spider-Man: No Way Home", "Spider-Man", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/81446973", 0xFFE5484D, R.drawable.ic_dock_appletv, R.drawable.fav_spiderman),
        new TitleItem("How I Met Your Mother", "Barney Stinson", "JioHotstar", "in.startv.hotstar", "https://www.hotstar.com/in/shows/how-i-met-your-mother/1260005597", 0xFFFA5252, R.drawable.ic_dock_hotstar, R.drawable.fav_barney)
    );

    public static List<Mood> getMoods() {
        List<TitleItem> comfort = Arrays.asList(
            new TitleItem("The Office", "Michael Scott", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70136120", 0xFFD28D40, R.drawable.ic_dock_netflix),
            new TitleItem("The Big Bang Theory", "Sheldon", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70143830", 0xFFD28D40, R.drawable.ic_dock_netflix),
            new TitleItem("How I Met Your Mother", "Barney", "JioHotstar", "in.startv.hotstar", "https://www.hotstar.com/in/shows/how-i-met-your-mother/1260005597", 0xFFD28D40, R.drawable.ic_dock_hotstar),
            new TitleItem("Brooklyn Nine-Nine", "Jake Peralta", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70281561", 0xFFD28D40, R.drawable.ic_dock_netflix),
            new TitleItem("Friends", "Chandler", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70153404", 0xFFD28D40, R.drawable.ic_dock_netflix)
        );

        List<TitleItem> capes = Arrays.asList(
            new TitleItem("Spider-Man: No Way Home", "Spider-Man", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/81446973", 0xFFE5484D, R.drawable.ic_dock_netflix),
            new TitleItem("The Flash", "Barry Allen", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/80027042", 0xFFE5484D, R.drawable.ic_dock_netflix),
            new TitleItem("The Boys", "Homelander", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com/detail?gti=amzn1.dv.gti.theboys", 0xFFE5484D, R.drawable.ic_dock_prime),
            new TitleItem("Daredevil", "Matt Murdock", "JioHotstar", "in.startv.hotstar", "https://www.hotstar.com", 0xFFE5484D, R.drawable.ic_dock_hotstar)
        );

        List<TitleItem> gotham = Arrays.asList(
            new TitleItem("The Dark Knight", "Batman", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70079583", 0xFF3B82F6, R.drawable.ic_dock_netflix),
            new TitleItem("The Batman", "Bruce Wayne", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com", 0xFF3B82F6, R.drawable.ic_dock_prime),
            new TitleItem("Joker", "Arthur Fleck", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com", 0xFF3B82F6, R.drawable.ic_dock_prime)
        );

        List<TitleItem> mass = Arrays.asList(
            new TitleItem("Master", "JD", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com/detail?gti=amzn1.dv.gti.master", 0xFFFF922B, R.drawable.ic_dock_prime),
            new TitleItem("Leo", "Parthiban", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/81639323", 0xFFFF922B, R.drawable.ic_dock_netflix),
            new TitleItem("Mersal", "Maaran", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/80220000", 0xFFFF922B, R.drawable.ic_dock_netflix)
        );

        List<TitleItem> mindGames = Arrays.asList(
            new TitleItem("The Mentalist", "Patrick Jane", "Prime Video", "com.amazon.amazonvideo.livingroom", "https://app.primevideo.com", 0xFF8B5CF6, R.drawable.ic_dock_prime),
            new TitleItem("Breaking Bad", "Walter White", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70143836", 0xFF8B5CF6, R.drawable.ic_dock_netflix),
            new TitleItem("Inception", "Dom Cobb", "Netflix", "com.netflix.ninja", "https://www.netflix.com/title/70131314", 0xFF8B5CF6, R.drawable.ic_dock_netflix)
        );

        List<TitleItem> allTitles = new ArrayList<>();
        allTitles.addAll(comfort);
        allTitles.addAll(capes);
        allTitles.addAll(gotham);
        allTitles.addAll(mass);
        allTitles.addAll(mindGames);

        return Arrays.asList(
            new Mood("Comfort sitcom", 0xFFD28D40, 6, "The Office • Friends • B99", comfort),
            new Mood("Capes and chaos", 0xFFE5484D, 7, "Spider-Man • The Flash • The Boys", capes),
            new Mood("Gotham after dark", 0xFF3B82F6, 4, "The Dark Knight • The Batman • Joker", gotham),
            new Mood("Thalapathy mass", 0xFFF97316, 6, "Master • Leo • Mersal", mass),
            new Mood("Mind games", 0xFF8B5CF6, 5, "Mentalist • Breaking Bad • Inception", mindGames),
            new Mood("Anything at all", 0xFF94A3B8, 28, "28 Trending Titles from Your Apps", allTitles)
        );
    }

    private static boolean isAppInstalled(PackageManager pm, String pkg) {
        try {
            pm.getPackageInfo(pkg, 0);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static void smartLaunchTitle(Context ctx, TitleItem item) {
        PackageManager pm = ctx.getPackageManager();
        boolean hasNetflix = isAppInstalled(pm, "com.netflix.ninja");
        boolean hasPrime = isAppInstalled(pm, "com.amazon.amazonvideo.livingroom");
        boolean hasHotstar = isAppInstalled(pm, "in.startv.hotstar");
        boolean hasAppleTv = isAppInstalled(pm, "com.apple.atve.androidtv.appletv");

        Intent launchIntent = null;

        if ("The Flash".equals(item.title) || "Reverse-Flash".equals(item.character)) {
            if (hasNetflix) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.netflix.com/title/80027042"));
                launchIntent.setPackage("com.netflix.ninja");
            } else if (hasPrime) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://app.primevideo.com/detail?gti=amzn1.dv.gti.theflash"));
                launchIntent.setPackage("com.amazon.amazonvideo.livingroom");
            }
        } else if ("The Mentalist".equals(item.title) || "Patrick Jane".equals(item.character)) {
            if (hasPrime) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://app.primevideo.com/detail?gti=amzn1.dv.gti.mentalist"));
                launchIntent.setPackage("com.amazon.amazonvideo.livingroom");
            } else if (hasNetflix) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.netflix.com/search?q=The%20Mentalist"));
                launchIntent.setPackage("com.netflix.ninja");
            }
        } else if ("Breaking Bad".equals(item.title)) {
            if (hasNetflix) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.netflix.com/title/70143836"));
                launchIntent.setPackage("com.netflix.ninja");
            }
        } else if ("The Big Bang Theory".equals(item.title)) {
            if (hasNetflix) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.netflix.com/title/70143830"));
                launchIntent.setPackage("com.netflix.ninja");
            }
        } else if ("Master".equals(item.title)) {
            if (hasPrime) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://app.primevideo.com/detail?gti=amzn1.dv.gti.master"));
                launchIntent.setPackage("com.amazon.amazonvideo.livingroom");
            }
        } else if ("Spider-Man: No Way Home".equals(item.title)) {
            if (hasNetflix) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.netflix.com/title/81446973"));
                launchIntent.setPackage("com.netflix.ninja");
            } else if (hasAppleTv) {
                launchIntent = pm.getLaunchIntentForPackage("com.apple.atve.androidtv.appletv");
            }
        } else if ("How I Met Your Mother".equals(item.title)) {
            if (hasHotstar) {
                launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.hotstar.com/in/shows/how-i-met-your-mother/1260005597"));
                launchIntent.setPackage("in.startv.hotstar");
            }
        }

        if (launchIntent == null && item.url != null) {
            launchIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(item.url));
            if (item.pkg != null && isAppInstalled(pm, item.pkg)) {
                launchIntent.setPackage(item.pkg);
            }
        }

        try {
            if (launchIntent != null) {
                launchIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                ctx.startActivity(launchIntent);
                return;
            }
        } catch (Exception ignored) {}

        if (item.pkg != null && isAppInstalled(pm, item.pkg)) {
            try {
                Intent fallback = pm.getLaunchIntentForPackage(item.pkg);
                if (fallback != null) {
                    fallback.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                    ctx.startActivity(fallback);
                    return;
                }
            } catch (Exception ignored) {}
        }

        Toast.makeText(ctx, "Opening " + item.title, Toast.LENGTH_SHORT).show();
    }

    private static void smoothScrollToSection(ScrollView mainScroll, View section) {
        if (mainScroll == null || section == null) return;
        mainScroll.post(() -> {
            int[] loc = new int[2];
            section.getLocationOnScreen(loc);
            int[] scrollLoc = new int[2];
            mainScroll.getLocationOnScreen(scrollLoc);
            int targetY = mainScroll.getScrollY() + (loc[1] - scrollLoc[1]);
            mainScroll.smoothScrollTo(0, Math.max(0, targetY));
        });
    }

    /**
     * ALL APPS ROW:
     */
    public static View createAppsRow(Activity activity, ScrollView mainScroll) {
        float density = activity.getResources().getDisplayMetrics().density;
        LinearLayout layout = new LinearLayout(activity);
        layout.setId(ID_APPS_ROW);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(Math.round(56 * density), Math.round(20 * density), Math.round(56 * density), Math.round(16 * density));
        layout.setClipChildren(false);
        layout.setClipToPadding(false);

        TextView header = new TextView(activity);
        header.setText("ALL APPS");
        header.setTextColor(0x8CFFFFFF);
        header.setTextSize(TypedValue.COMPLEX_UNIT_SP, 14);
        header.setLetterSpacing(0.12f);
        header.setTypeface(android.graphics.Typeface.create("sans-serif-medium", android.graphics.Typeface.NORMAL));
        header.setPadding(0, 0, 0, Math.round(14 * density));
        layout.addView(header);

        HorizontalScrollView scroll = new HorizontalScrollView(activity);
        scroll.setHorizontalScrollBarEnabled(false);
        scroll.setOverScrollMode(View.OVER_SCROLL_NEVER);
        scroll.setClipToPadding(false);
        scroll.setClipChildren(false);

        LinearLayout row = new LinearLayout(activity);
        row.setOrientation(LinearLayout.HORIZONTAL);
        row.setClipToPadding(false);
        row.setClipChildren(false);

        PackageManager pm = activity.getPackageManager();
        String[] popularPkgs = {
            "com.android.vending",
            "com.mxtech.videoplayer.television",
            "com.sonyliv",
            "com.jio.media.stb.ondemand.xiaomi",
            "com.graymatrix.did",
            "com.yablio.sendfilestotv",
            "com.jio.web.androidtv",
            "com.android.tv.settings"
        };

        boolean first = true;
        for (String pkg : popularPkgs) {
            Drawable icon = null;
            String name = pkg;
            try {
                ApplicationInfo ai = pm.getApplicationInfo(pkg, 0);
                icon = pm.getApplicationBanner(ai);
                if (icon == null) icon = pm.getApplicationIcon(ai);
                name = pm.getApplicationLabel(ai).toString();
            } catch (Exception e) {
                if (!"com.android.vending".equals(pkg) && !"com.android.tv.settings".equals(pkg)) continue;
                if ("com.android.vending".equals(pkg)) name = "Play Store";
                if ("com.android.tv.settings".equals(pkg)) name = "Settings";
            }

            FrameLayout card = new FrameLayout(activity);
            if (first) {
                card.setId(10011);
                first = false;
            }
            card.setFocusable(true);
            card.setClickable(true);
            card.setNextFocusUpId(R.id.grid);
            card.setNextFocusDownId(10021); // First card of Section 6

            int cw = Math.round(172 * density);
            int ch = Math.round(74 * density);
            LinearLayout.LayoutParams clp = new LinearLayout.LayoutParams(cw, ch);
            clp.setMargins(Math.round(8 * density), 0, Math.round(8 * density), 0);
            card.setLayoutParams(clp);

            GradientDrawable normBg = new GradientDrawable();
            normBg.setShape(GradientDrawable.RECTANGLE);
            normBg.setCornerRadius(14 * density);
            normBg.setColor(0x28FFFFFF);
            normBg.setStroke(Math.round(1 * density), 0x2EFFFFFF);

            GradientDrawable focBg = new GradientDrawable();
            focBg.setShape(GradientDrawable.RECTANGLE);
            focBg.setCornerRadius(14 * density);
            focBg.setColor(0x4DFFFFFF);
            focBg.setStroke(Math.round(2.5f * density), Color.WHITE);

            card.setBackground(normBg);

            LinearLayout content = new LinearLayout(activity);
            content.setOrientation(LinearLayout.HORIZONTAL);
            content.setGravity(Gravity.CENTER);
            content.setPadding(Math.round(12 * density), Math.round(8 * density), Math.round(12 * density), Math.round(8 * density));

            ImageView iv = new ImageView(activity);
            int iconSize = Math.round(36 * density);
            LinearLayout.LayoutParams ivLp = new LinearLayout.LayoutParams(iconSize, iconSize);
            ivLp.setMarginEnd(Math.round(10 * density));
            iv.setLayoutParams(ivLp);
            if (icon != null) iv.setImageDrawable(icon);
            else if ("com.android.vending".equals(pkg)) iv.setImageResource(R.drawable.ic_apps_pill);
            else iv.setImageResource(R.drawable.ic_settings);
            iv.setScaleType(ImageView.ScaleType.FIT_CENTER);
            content.addView(iv);

            TextView tv = new TextView(activity);
            tv.setText(name);
            tv.setTextColor(Color.WHITE);
            tv.setTextSize(TypedValue.COMPLEX_UNIT_SP, 13);
            tv.setTypeface(android.graphics.Typeface.create("sans-serif-medium", android.graphics.Typeface.NORMAL));
            tv.setSingleLine(true);
            tv.setEllipsize(android.text.TextUtils.TruncateAt.END);
            content.addView(tv);

            card.addView(content);

            final String finalPkg = pkg;
            card.setOnClickListener(v -> {
                try {
                    Intent it = pm.getLaunchIntentForPackage(finalPkg);
                    if (it != null) {
                        it.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                        activity.startActivity(it);
                    } else if ("com.android.tv.settings".equals(finalPkg)) {
                        activity.startActivity(new Intent(android.provider.Settings.ACTION_SETTINGS));
                    }
                } catch (Exception ex) {
                    Toast.makeText(activity, "Launching...", Toast.LENGTH_SHORT).show();
                }
            });

            card.setOnFocusChangeListener((v, hasFocus) -> {
                if (hasFocus) {
                    card.setBackground(focBg);
                    card.animate().scaleX(1.10f).scaleY(1.10f).setDuration(200).start();
                    if (activity instanceof MainActivity) {
                        ((MainActivity) activity).hideHero();
                    }
                    smoothScrollToSection(mainScroll, layout);
                } else {
                    card.setBackground(normBg);
                    card.animate().scaleX(1.0f).scaleY(1.0f).setDuration(160).start();
                }
            });

            row.addView(card);
        }

        scroll.addView(row);
        layout.addView(scroll);
        return layout;
    }

    /**
     * Section 6: My Favourites (Page 2)
     */
    public static View createFavouritesRow(Activity activity, ScrollView mainScroll) {
        float density = activity.getResources().getDisplayMetrics().density;
        LinearLayout section = new LinearLayout(activity);
        section.setId(ID_FAV_ROW);
        section.setOrientation(LinearLayout.VERTICAL);
        section.setClipChildren(false);
        section.setClipToPadding(false);

        LinearLayout headerBar = new LinearLayout(activity);
        headerBar.setOrientation(LinearLayout.HORIZONTAL);
        headerBar.setGravity(Gravity.CENTER_VERTICAL);
        headerBar.setPadding(Math.round(56 * density), Math.round(18 * density), Math.round(56 * density), Math.round(6 * density));

        TextView secTitle = new TextView(activity);
        secTitle.setText("My Favourites");
        secTitle.setTextColor(0xD9FFFFFF);
        secTitle.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20);
        secTitle.setTypeface(android.graphics.Typeface.create("sans-serif-light", android.graphics.Typeface.NORMAL));
        headerBar.addView(secTitle);

        View spacer = new View(activity);
        LinearLayout.LayoutParams spacerLp = new LinearLayout.LayoutParams(Math.round(32 * density), 1);
        headerBar.addView(spacer, spacerLp);

        TextView favTitle = new TextView(activity);
        favTitle.setText("The Mentalist");
        favTitle.setTextColor(Color.WHITE);
        favTitle.setTextSize(TypedValue.COMPLEX_UNIT_SP, 22);
        favTitle.setTypeface(android.graphics.Typeface.create("sans-serif", android.graphics.Typeface.NORMAL));
        favTitle.setSingleLine(true);
        headerBar.addView(favTitle);

        ImageView appBadge = new ImageView(activity);
        int badgeSize = Math.round(20 * density);
        LinearLayout.LayoutParams badgeLp = new LinearLayout.LayoutParams(badgeSize, badgeSize);
        badgeLp.setMarginStart(Math.round(12 * density));
        appBadge.setLayoutParams(badgeLp);
        appBadge.setImageResource(R.drawable.ic_dock_prime);
        headerBar.addView(appBadge);

        section.addView(headerBar);

        FrameLayout stage = new FrameLayout(activity);
        int stageH = Math.round(340 * density);
        LinearLayout.LayoutParams stageLp = new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, stageH);
        stageLp.setMargins(0, Math.round(4 * density), 0, Math.round(16 * density));
        stage.setLayoutParams(stageLp);

        ImageView backdrop = new ImageView(activity);
        backdrop.setLayoutParams(new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        backdrop.setScaleType(ImageView.ScaleType.CENTER_CROP);
        backdrop.setImageResource(R.drawable.fav_mentalist);
        stage.addView(backdrop);

        LinearLayout charRow = new LinearLayout(activity);
        charRow.setOrientation(LinearLayout.HORIZONTAL);
        charRow.setGravity(Gravity.CENTER);
        charRow.setClipChildren(false);
        charRow.setClipToPadding(false);

        FrameLayout.LayoutParams charRowLp = new FrameLayout.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            Gravity.BOTTOM | Gravity.CENTER_HORIZONTAL
        );
        charRowLp.bottomMargin = Math.round(12 * density);
        charRow.setLayoutParams(charRowLp);

        for (int i = 0; i < FAVOURITES.size(); i++) {
            final TitleItem item = FAVOURITES.get(i);
            FrameLayout charCard = new FrameLayout(activity);
            if (i == 0) charCard.setId(10021);
            charCard.setFocusable(true);
            charCard.setClickable(true);
            charCard.setNextFocusUpId(10011); // To ALL APPS row
            charCard.setNextFocusDownId(10031); // To Mood cards

            int cw = Math.round(112 * density);
            int ch = Math.round(42 * density);
            LinearLayout.LayoutParams clp = new LinearLayout.LayoutParams(cw, ch);
            clp.setMargins(Math.round(6 * density), 0, Math.round(6 * density), 0);
            charCard.setLayoutParams(clp);

            GradientDrawable normBg = new GradientDrawable();
            normBg.setShape(GradientDrawable.RECTANGLE);
            normBg.setCornerRadius(21 * density);
            normBg.setColor(0x33000000);
            normBg.setStroke(Math.round(1 * density), 0x26FFFFFF);

            GradientDrawable focBg = new GradientDrawable();
            focBg.setShape(GradientDrawable.RECTANGLE);
            focBg.setCornerRadius(21 * density);
            focBg.setColor(0x66000000 | (item.color & 0x00FFFFFF));
            focBg.setStroke(Math.round(2 * density), item.color);

            charCard.setBackground(normBg);

            TextView charName = new TextView(activity);
            charName.setText(item.character);
            charName.setTextColor(Color.WHITE);
            charName.setTextSize(TypedValue.COMPLEX_UNIT_SP, 12);
            charName.setGravity(Gravity.CENTER);
            charName.setSingleLine(true);
            FrameLayout.LayoutParams cnlp = new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT);
            charCard.addView(charName, cnlp);

            charCard.setOnClickListener(v -> smartLaunchTitle(activity, item));

            charCard.setOnFocusChangeListener((v, hasFocus) -> {
                if (hasFocus) {
                    charCard.setBackground(focBg);
                    charCard.animate().scaleX(1.14f).scaleY(1.14f).setDuration(220).start();

                    favTitle.setText(item.title);
                    if (item.appIconRes != 0) appBadge.setImageResource(item.appIconRes);

                    if (item.sceneRes != 0) {
                        backdrop.setImageResource(item.sceneRes);
                    } else {
                        backdrop.setImageResource(R.drawable.fav_lineup_bw);
                    }

                    if (activity instanceof MainActivity) {
                        ((MainActivity) activity).hideHero();
                    }

                    smoothScrollToSection(mainScroll, section);
                } else {
                    charCard.setBackground(normBg);
                    charCard.animate().scaleX(1.0f).scaleY(1.0f).setDuration(160).start();
                }
            });

            charRow.addView(charCard);
        }

        stage.addView(charRow);
        section.addView(stage);

        return section;
    }

    /**
     * Section 7: Don't have time to browse? (Page 3)
     */
    public static View createMoodsRow(Activity activity, ScrollView mainScroll) {
        float density = activity.getResources().getDisplayMetrics().density;
        LinearLayout section = new LinearLayout(activity);
        section.setId(ID_MOODS_ROW);
        section.setOrientation(LinearLayout.VERTICAL);
        section.setPadding(Math.round(56 * density), Math.round(24 * density), Math.round(56 * density), Math.round(24 * density));
        section.setClipChildren(false);
        section.setClipToPadding(false);

        TextView header = new TextView(activity);
        header.setText("Don't have time to browse?");
        header.setTextColor(0x8CFFFFFF);
        header.setTextSize(TypedValue.COMPLEX_UNIT_SP, 16);
        header.setTypeface(android.graphics.Typeface.create("sans-serif", android.graphics.Typeface.NORMAL));
        header.setGravity(Gravity.CENTER);
        header.setPadding(0, 0, 0, Math.round(24 * density));
        section.addView(header);

        HorizontalScrollView scroll = new HorizontalScrollView(activity);
        scroll.setHorizontalScrollBarEnabled(false);
        scroll.setOverScrollMode(View.OVER_SCROLL_NEVER);
        scroll.setClipToPadding(false);
        scroll.setClipChildren(false);

        LinearLayout row = new LinearLayout(activity);
        row.setOrientation(LinearLayout.HORIZONTAL);
        row.setClipToPadding(false);
        row.setClipChildren(false);

        boolean first = true;
        for (Mood mood : getMoods()) {
            FrameLayout card = new FrameLayout(activity);
            if (first) {
                card.setId(10031);
                first = false;
            }
            card.setFocusable(true);
            card.setClickable(true);
            card.setNextFocusUpId(10021); // To Section 6 characters
            card.setNextFocusDownId(ID_MORE_APPS); // To More Apps button

            int cw = Math.round(176 * density);
            int ch = Math.round(216 * density);
            LinearLayout.LayoutParams clp = new LinearLayout.LayoutParams(cw, ch);
            clp.setMargins(Math.round(10 * density), Math.round(8 * density), Math.round(10 * density), Math.round(8 * density));
            card.setLayoutParams(clp);

            GradientDrawable normBg = new GradientDrawable();
            normBg.setShape(GradientDrawable.RECTANGLE);
            normBg.setCornerRadius(16 * density);
            normBg.setColor(0xCC0E1015);
            normBg.setStroke(Math.round(1.5f * density), (mood.color & 0x00FFFFFF) | 0x4D000000);

            GradientDrawable focBg = new GradientDrawable();
            focBg.setShape(GradientDrawable.RECTANGLE);
            focBg.setCornerRadius(16 * density);
            focBg.setColor(0xE60E1015);
            focBg.setStroke(Math.round(2.5f * density), mood.color);

            card.setBackground(normBg);

            LinearLayout content = new LinearLayout(activity);
            content.setOrientation(LinearLayout.VERTICAL);
            content.setGravity(Gravity.CENTER);
            content.setPadding(Math.round(14 * density), Math.round(16 * density), Math.round(14 * density), Math.round(16 * density));

            View dot = new View(activity);
            int dotSize = Math.round(26 * density);
            GradientDrawable dotBg = new GradientDrawable();
            dotBg.setShape(GradientDrawable.OVAL);
            dotBg.setColor(mood.color);
            dot.setBackground(dotBg);
            LinearLayout.LayoutParams dotLp = new LinearLayout.LayoutParams(dotSize, dotSize);
            dotLp.bottomMargin = Math.round(14 * density);
            content.addView(dot, dotLp);

            TextView txtTitle = new TextView(activity);
            txtTitle.setText(mood.name);
            txtTitle.setTextColor(0xF2FFFFFF);
            txtTitle.setTextSize(TypedValue.COMPLEX_UNIT_SP, 17);
            txtTitle.setTypeface(android.graphics.Typeface.create("sans-serif-medium", android.graphics.Typeface.NORMAL));
            txtTitle.setGravity(Gravity.CENTER);
            content.addView(txtTitle);

            TextView txtSug = new TextView(activity);
            txtSug.setText(mood.suggestions);
            txtSug.setTextColor(0xB3FFFFFF);
            txtSug.setTextSize(TypedValue.COMPLEX_UNIT_SP, 11);
            txtSug.setGravity(Gravity.CENTER);
            txtSug.setPadding(0, Math.round(6 * density), 0, 0);
            content.addView(txtSug);

            TextView txtCount = new TextView(activity);
            txtCount.setText(mood.count + " titles");
            txtCount.setTextColor(mood.color);
            txtCount.setTextSize(TypedValue.COMPLEX_UNIT_SP, 12);
            txtCount.setGravity(Gravity.CENTER);
            txtCount.setPadding(0, Math.round(8 * density), 0, 0);
            content.addView(txtCount);

            card.addView(content);

            card.setOnClickListener(v -> showMoodRoulette(activity, mood));

            card.setOnFocusChangeListener((v, hasFocus) -> {
                if (hasFocus) {
                    card.setBackground(focBg);
                    card.animate().scaleX(1.08f).scaleY(1.08f).setDuration(220).start();
                    if (activity instanceof MainActivity) {
                        ((MainActivity) activity).hideHero();
                    }
                    smoothScrollToSection(mainScroll, section);
                } else {
                    card.setBackground(normBg);
                    card.animate().scaleX(1.0f).scaleY(1.0f).setDuration(160).start();
                }
            });

            row.addView(card);
        }

        scroll.addView(row);
        section.addView(scroll);

        View moreApps = createMoreAppsButton(activity);
        section.addView(moreApps);

        return section;
    }

    public static void showMoodRoulette(Activity activity, Mood mood) {
        if (mood.titles == null || mood.titles.isEmpty()) return;

        AlertDialog.Builder builder = new AlertDialog.Builder(activity);
        LinearLayout root = new LinearLayout(activity);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(64, 48, 64, 48);
        root.setGravity(Gravity.CENTER);
        root.setBackgroundColor(0xF20A0D14);

        TextView header = new TextView(activity);
        header.setText(mood.name.toUpperCase());
        header.setTextColor(mood.color);
        header.setTextSize(TypedValue.COMPLEX_UNIT_SP, 16);
        header.setLetterSpacing(0.15f);
        root.addView(header);

        TextView reelTitle = new TextView(activity);
        reelTitle.setText("SPINNING REEL…");
        reelTitle.setTextColor(Color.WHITE);
        reelTitle.setTextSize(TypedValue.COMPLEX_UNIT_SP, 30);
        reelTitle.setGravity(Gravity.CENTER);
        reelTitle.setPadding(0, 32, 0, 12);
        root.addView(reelTitle);

        TextView subMeta = new TextView(activity);
        subMeta.setText("Picking from " + mood.titles.size() + " titles");
        subMeta.setTextColor(0xB3FFFFFF);
        subMeta.setTextSize(TypedValue.COMPLEX_UNIT_SP, 15);
        root.addView(subMeta);

        TextView countdownText = new TextView(activity);
        countdownText.setTextColor(mood.color);
        countdownText.setTextSize(TypedValue.COMPLEX_UNIT_SP, 18);
        countdownText.setPadding(0, 24, 0, 0);
        countdownText.setVisibility(View.GONE);
        root.addView(countdownText);

        builder.setView(root);
        AlertDialog dialog = builder.create();
        dialog.show();

        Handler handler = new Handler(Looper.getMainLooper());
        Random random = new Random();
        final int[] spinCount = {0};
        final int totalSpins = 16;
        final TitleItem[] chosen = {mood.titles.get(random.nextInt(mood.titles.size()))};

        Runnable spinRunnable = new Runnable() {
            @Override
            public void run() {
                if (spinCount[0] < totalSpins) {
                    TitleItem candidate = mood.titles.get(random.nextInt(mood.titles.size()));
                    reelTitle.setText(candidate.title);
                    subMeta.setText(candidate.character + " · " + candidate.app);
                    spinCount[0]++;
                    long delay = 60 + (spinCount[0] * spinCount[0] * 3);
                    handler.postDelayed(this, delay);
                } else {
                    chosen[0] = mood.titles.get(random.nextInt(mood.titles.size()));
                    reelTitle.setText(chosen[0].title);
                    subMeta.setText(chosen[0].character + " · " + chosen[0].app);
                    countdownText.setVisibility(View.VISIBLE);

                    final int[] seconds = {3};
                    Runnable countRunnable = new Runnable() {
                        @Override
                        public void run() {
                            if (seconds[0] > 0) {
                                countdownText.setText("Opening in " + seconds[0] + "… OK to play now · > spin again");
                                seconds[0]--;
                                handler.postDelayed(this, 1000);
                            } else {
                                if (dialog.isShowing()) {
                                    dialog.dismiss();
                                    smartLaunchTitle(activity, chosen[0]);
                                }
                            }
                        }
                    };
                    handler.post(countRunnable);

                    root.setOnClickListener(v -> {
                        handler.removeCallbacksAndMessages(null);
                        dialog.dismiss();
                        smartLaunchTitle(activity, chosen[0]);
                    });
                }
            }
        };
        handler.post(spinRunnable);
    }

    public static View createMoreAppsButton(Activity activity) {
        float density = activity.getResources().getDisplayMetrics().density;
        LinearLayout container = new LinearLayout(activity);
        container.setGravity(Gravity.CENTER);
        container.setPadding(0, Math.round(28 * density), 0, Math.round(36 * density));

        FrameLayout pill = new FrameLayout(activity);
        pill.setId(ID_MORE_APPS);
        pill.setFocusable(true);
        pill.setClickable(true);
        pill.setNextFocusUpId(10031); // To Mood cards

        int w = Math.round(164 * density);
        int h = Math.round(44 * density);
        pill.setLayoutParams(new LinearLayout.LayoutParams(w, h));

        GradientDrawable normalBg = new GradientDrawable();
        normalBg.setShape(GradientDrawable.RECTANGLE);
        normalBg.setCornerRadius(22 * density);
        normalBg.setColor(0x1FFFFFFF);
        normalBg.setStroke(Math.round(1 * density), 0x29FFFFFF);

        GradientDrawable focusBg = new GradientDrawable();
        focusBg.setShape(GradientDrawable.RECTANGLE);
        focusBg.setCornerRadius(22 * density);
        focusBg.setColor(0x3FFFFFFF);
        focusBg.setStroke(Math.round(2 * density), Color.WHITE);

        pill.setBackground(normalBg);

        LinearLayout row = new LinearLayout(activity);
        row.setOrientation(LinearLayout.HORIZONTAL);
        row.setGravity(Gravity.CENTER);

        TextView icon = new TextView(activity);
        icon.setText("㗊 ");
        icon.setTextColor(Color.WHITE);
        icon.setTextSize(TypedValue.COMPLEX_UNIT_SP, 15);
        row.addView(icon);

        TextView label = new TextView(activity);
        label.setText("More apps");
        label.setTextColor(Color.WHITE);
        label.setTextSize(TypedValue.COMPLEX_UNIT_SP, 15);
        label.setTypeface(android.graphics.Typeface.create("sans-serif-medium", android.graphics.Typeface.NORMAL));
        row.addView(label);

        pill.addView(row);

        pill.setOnClickListener(v -> {
            if (activity instanceof MainActivity) {
                ((MainActivity) activity).onLibraryRequested();
            }
        });

        pill.setOnFocusChangeListener((v, hasFocus) -> {
            if (hasFocus) {
                pill.setBackground(focusBg);
                pill.animate().scaleX(1.08f).scaleY(1.08f).setDuration(220).start();
                if (activity instanceof MainActivity) {
                    ((MainActivity) activity).hideHero();
                }
            } else {
                pill.setBackground(normalBg);
                pill.animate().scaleX(1.0f).scaleY(1.0f).setDuration(160).start();
            }
        });

        container.addView(pill);
        return container;
    }
}
