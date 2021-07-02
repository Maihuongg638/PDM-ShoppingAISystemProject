const gulp = require("gulp");
const plumber = require("gulp-plumber");
const rename = require("gulp-rename");
const sass = require("gulp-sass");
const autoPrefixer = require("gulp-autoprefixer");
require("es6-promise").polyfill();
const cssComb = require("gulp-csscomb");
const cmq = require("gulp-merge-media-queries");
const cleanCss = require("gulp-clean-css");
(browserSync = require("browser-sync").create()), (reload = browserSync.reload);
const uglify = require("gulp-uglify-es").default;

const imagemin = require("gulp-imagemin");

gulp.task("scss", function () {
  return gulp
    .src(["src/scss/**/*.scss"])
    .pipe(sass())
    .pipe(autoPrefixer())
    .pipe(cssComb())
    .pipe(cmq({ log: true }))
    .pipe(gulp.dest("dist/css"))
    .pipe(
      rename({
        suffix: ".min",
      })
    )
    .pipe(cleanCss())
    .pipe(gulp.dest("dist/css"));
});

gulp.task("image", function () {
  return gulp.src("src/img/*").pipe(imagemin()).pipe(gulp.dest("dist/img"));
});

gulp.task("js", function () {
  return gulp
    .src(["src/js/**/*.js"])
    .pipe(gulp.dest("dist/js"))
    .pipe(
      rename({
        suffix: ".min",
      })
    )
    .pipe(uglify())
    .pipe(gulp.dest("dist/js"));
});

gulp.task("serve", function () {
  // Serve files from the root of this project
  browserSync.init({
    server: {
      baseDir: ".",
    },
  });

  gulp.watch("src/js/**/*.js", gulp.series("js")).on("change", reload);
  gulp.watch("src/scss/**/*.scss", gulp.series("scss")).on("change", reload);
  gulp.watch("src/img/*", gulp.series("image")).on("change", reload);
  gulp.watch("*.html").on("change", reload);
});
