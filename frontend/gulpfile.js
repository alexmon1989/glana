const gulp          = require('gulp'), // Gulp
    sass            = require('gulp-sass'), // SASS,
    autoprefixer    = require('gulp-autoprefixer'), // Add the desired vendor prefixes and remove unnecessary in SASS-files
    browserSync     = require('browser-sync'),
    gutil           = require('gulp-util'),
    cleanCSS        = require('gulp-clean-css'),
    concat          = require('gulp-concat'),
    del             = require('del'),
    imagemin        = require('gulp-imagemin'),
    cache           = require('gulp-cache'),
    uglify          = require('gulp-uglify'),
    njkRender       = require('gulp-nunjucks-render'),
    htmlbeautify    = require('gulp-html-beautify');

const config = {
    srcDir: './app',
    distDir: './dist',
    sassPattern: 'scss/**/*.scss',
    jsPattern: 'js/**/*.js',
    imgPattern: 'img/**/*.*',
    njkPattern: 'nunjucks/**/*.njk'
};


//
// Fonts
//
gulp.task('fonts', function () {
    return gulp.src([
        config.srcDir + '/vendor/icon-awesome/fonts/*.*',
        config.srcDir + '/vendor/icon-hs/fonts/*.*'
    ]).pipe(gulp.dest(config.srcDir + '/fonts/'));
});


//
// Сборка стилей
//

gulp.task('sass', function() {
    return gulp.src(config.srcDir + '/scss/main.scss')
        .pipe(sass({outputStyle: 'expand'}))
        .pipe(autoprefixer(['last 15 versions']))
        .pipe(gulp.dest(config.srcDir + '/css/'))
});

gulp.task('css', ['fonts', 'sass'], function () {
    return gulp.src([
        config.srcDir + '/vendor/bootstrap/bootstrap.min.css',
        config.srcDir + '/vendor/icon-awesome/css/font-awesome.min.css',
        config.srcDir + '/vendor/icon-hs/style.css',
        config.srcDir + '/vendor/dzsparallaxer/dzsparallaxer.css',
        config.srcDir + '/vendor/dzsparallaxer/dzsscroller/scroller.css',
        config.srcDir + '/vendor/dzsparallaxer/advancedscroller/plugin.css',
        config.srcDir + '/vendor/hs-megamenu/src/hs.megamenu.css',
        config.srcDir + '/vendor/slick-carousel/slick/slick.css',
        config.srcDir + '/vendor/hamburgers/hamburgers.min.css',
        config.srcDir + '/vendor/cubeportfolio-full/cubeportfolio/css/cubeportfolio.min.css',
        config.srcDir + '/vendor/animate.css',
        config.srcDir + '/vendor/custombox/custombox.min.css',
        config.srcDir + '/css/main.css'
    ])
        .pipe(concat('bundle.min.css'))
        .pipe(gulp.dest(config.srcDir + '/css/'))
        .pipe(browserSync.reload({stream: true}));
});


//
// Сборка JS
//

gulp.task('js', function () {
    return gulp.src([
        config.srcDir + '/vendor/jquery/jquery.min.js',
        config.srcDir + '/vendor/jquery-migrate/jquery-migrate.min.js',
        config.srcDir + '/vendor/popper.min.js',
        config.srcDir + '/vendor/bootstrap/bootstrap.min.js',
        config.srcDir + '/vendor/hs-megamenu/src/hs.megamenu.js',		
        config.srcDir + '/vendor/dzsparallaxer/dzsparallaxer.js',
        config.srcDir + '/vendor/dzsparallaxer/dzsscroller/scroller.js',
        config.srcDir + '/vendor/dzsparallaxer/advancedscroller/plugin.js',
        config.srcDir + '/vendor/imagesloaded/imagesloaded.pkgd.min.js',
        config.srcDir + '/vendor/slick-carousel/slick/slick.js',
        config.srcDir + '/vendor/cubeportfolio-full/cubeportfolio/js/jquery.cubeportfolio.min.js',
        config.srcDir + '/vendor/jquery.form.js',
        config.srcDir + '/vendor/jquery-validation/dist/jquery.validate.js',
        config.srcDir + '/vendor/custombox/custombox.min.js',
        config.srcDir + '/vendor/jquery.scrollTo.min.js',
        config.srcDir + '/js/hs.core.js',
        config.srcDir + '/js/components/hs.header.js',
        config.srcDir + '/js/helpers/hs.hamburgers.js',
        config.srcDir + '/js/components/hs.carousel.js',
        config.srcDir + '/js/components/hs.dropdown.js',
        config.srcDir + '/js/components/hs.scroll-nav.js',
        config.srcDir + '/js/components/hs.cubeportfolio.js',
        config.srcDir + '/js/helpers/hs.file-attachments.js',
        config.srcDir + '/js/components/hs.validation.js',
        config.srcDir + '/js/components/hs.modal-window.js',
        config.srcDir + '/js/components/hs.go-to.js',
        config.srcDir + '/js/components/hs.tabs.js',
        config.srcDir + '/js/custom.js'
    ])
        .pipe(concat('bundle.min.js'))
        .pipe(gulp.dest(config.srcDir + '/js/'))
        .pipe(browserSync.reload({stream: true}));
});

//
// Browser Sync
//

gulp.task('browser-sync', function () {
    browserSync({
        server: {
            baseDir: config.srcDir
        },
        notify: false
        // tunnel: true,
        // tunnel: "projectmane", //Demonstration page: http://projectmane.localtunnel.me
    });
});


//
// Nunjucks
//

gulp.task('nunjucks', function () {
    return gulp.src([
        config.srcDir + '/nunjucks/index.njk'
    ])
        .pipe(njkRender())
        .pipe(htmlbeautify({
            indent_size : 4 // размер отступа - 4 пробела
        }))
        .pipe(gulp.dest('./app'))
        .pipe(browserSync.reload({stream: true}));
});


//
// Images
//

gulp.task('imagemin', function () {
    return gulp.src([
        config.srcDir + '/' + config.imgPattern
    ])
        .pipe(cache(imagemin())) // Cache Images
        .pipe(gulp.dest(config.distDir + '/img'));
});

gulp.task('removedist', function () {
    return del.sync('dist');
});

gulp.task('clearcache', function () {
    return cache.clearAll();
});

//
// Watch
//

gulp.task('watch', function() {
  gulp.watch(config.srcDir + '/' + config.sassPattern, ['css']);
  gulp.watch(config.srcDir + '/' + config.jsPattern, ['js']);
  gulp.watch(config.srcDir + '/' + config.njkPattern, ['nunjucks']);
});


//
// Default
//

gulp.task('default', ['watch', 'css', 'js', 'nunjucks', 'browser-sync']);


//
// Build
//

gulp.task('build', ['clearcache', 'removedist', 'js', 'css', 'nunjucks', 'imagemin'], function () {


    const buildCss = gulp.src([
        config.srcDir + '/css/bundle.min.css'
    ])
        .pipe(cleanCSS({level: {1: {specialComments: 0}}}))
        .pipe(gulp.dest(config.distDir + '/css'));

    const buildJs = gulp.src([
        config.srcDir + '/js/bundle.min.js'
    ])
        .pipe(uglify())
        .pipe(gulp.dest(config.distDir + '/js'));

    const buildFonts = gulp.src([
        config.srcDir + '/fonts/*.*'
    ]).pipe(gulp.dest(config.distDir + '/fonts'));

    const buildFiles = gulp.src([
        config.srcDir + '/*.html'
    ]).pipe(gulp.dest('dist'));

    // Другие файлы для сборки
    gulp.src([
        config.srcDir + '/vendor/dzsparallaxer/dzsscroller/styleimg/**/*.*'
    ]).pipe(gulp.dest(config.distDir + '/css/styleimg/'));
    gulp.src([
        config.srcDir + '/vendor/dzsparallaxer/advancedscroller/bokeh/**/*.*'
    ]).pipe(gulp.dest(config.distDir + '/css/bokeh/'));
    gulp.src([
        config.srcDir + '/vendor/dzsparallaxer/advancedscroller/img/**/*.*'
    ]).pipe(gulp.dest(config.distDir + '/css/img/'));


});


// Минификация загружаемых изображений товаров

gulp.task('imagemin-products', function () {
    return gulp.src([
        '../media/products/**/*.*'
    ])
        .pipe(imagemin())
        .pipe(gulp.dest('../media/products/'));
});
