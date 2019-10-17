module.exports = {
    css: {
        loaderOptions: {
            sass: {
                prependData: `
                    @import "@/styles/_variables.scss";
                    @import "@/styles/_spacing.scss";
                    @import "@/styles/_color.scss";
                    @import "@/styles/_btn.scss";
                    @import "@/styles/components/_signform.scss";
                    @import "@/styles/components/_nav.scss";
                    @import "@/styles/components/_footer.scss";
                    @import "@/styles/components/_sidebar.scss";
                    @import "@/styles/components/_listCard.scss";
                    @import "@/styles/view/_main.scss";
                    @import "@/styles/view/_category.scss";
                    @import "@/styles/view/_journal.scss";
                `
            }
        }
    }
}
