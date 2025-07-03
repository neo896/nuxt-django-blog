<template>
    <div class="relative">
        <img class="w-full h-80 object-cover"
            src="https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1400&q=80"
            alt="随机图片" />
        <div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-center text-white px-4">
            <h1 class="text-3xl md:text-5xl font-bold mb-2">Cael的博客</h1>
            <p class="text-base md:text-xl max-w-2xl">分享技术、生活与灵感，发现更大的世界。</p>
        </div>
    </div>

    <main class="max-w-7xl mx-auto py-6 px-4">
        <div class="relative mb-8">
            <div class="relative">
                <input
                    type="text"
                    placeholder="搜索文章..."
                    class="w-full pl-12 pr-4 py-3 text-base rounded-xl bg-gray-50 border border-gray-200 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent dark:bg-gray-800 dark:border-gray-700 dark:text-white transition-all duration-200"
                />
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <Icon name="heroicons:magnifying-glass" class="w-5 h-5 text-gray-400 dark:text-gray-500" />
                </div>
            </div>
        </div>

        <h2 class="text-2xl font-bold mb-4">最新文章</h2>
        <div class="grid gap-4 md:grid-cols-3">
            <ClientOnly>
                <CardContainer v-for="article in articles" :key="article.id" class="w-full">
                    <CardBody
                        class="group/card relative size-auto rounded-xl border border-black/[0.1] bg-gray-50 p-4 w-full dark:border-white/[0.2] dark:bg-black dark:hover:shadow-2xl dark:hover:shadow-emerald-500/[0.1] min-h-[400px] flex flex-col">
                        <div class="h-32 flex flex-col">
                            <CardItem :translate-z="50" class="text-lg font-bold text-neutral-600 dark:text-white">
                                {{ article.title }}
                            </CardItem>
                            <CardItem :translate-z="40" class="mt-2">
                                <span
                                    class="text-xs font-medium bg-emerald-100 text-emerald-700 px-2 py-1 rounded-full dark:bg-emerald-900/30 dark:text-emerald-400">
                                    {{ article.category }}
                                </span>
                            </CardItem>
                            <CardItem as="p" translate-z="60"
                                class="mt-2 max-w-sm text-sm text-neutral-500 dark:text-neutral-300 line-clamp-2">
                                {{ article.description }}
                            </CardItem>
                        </div>
                        <CardItem :translate-z="100" class="mt-2 w-full">
                            <img :src="article.image"
                                height="1000" width="1000"
                                class="h-40 w-full rounded-xl object-cover group-hover/card:shadow-xl"
                                :alt="article.title" />
                        </CardItem>
                        <div class="mt-auto pt-4 flex items-center justify-between">
                            <CardItem :translate-z="20">
                                <nuxt-link :to="`/article/${article.slug}`"
                                    class="rounded-xl px-4 py-2 text-sm font-bold dark:text-white hover:text-emerald-500 dark:hover:text-emerald-400 transition-colors">
                                    阅读全文 →
                                </nuxt-link>
                            </CardItem>
                            <CardItem :translate-z="20" class="rounded-xl px-4 py-2 text-sm font-normal dark:text-white">
                                {{ article.date }}
                            </CardItem>
                        </div>
                    </CardBody>
                </CardContainer>
            </ClientOnly>
        </div>
    </main>
</template>

<script lang="ts" setup>
import { CardContainer, CardBody, CardItem } from "@/components/ui/card-3d";

// 示例文章数据
const articles = [
    {
        id: 1,
        title: 'Make things float in air',
        slug: 'make-things-float-in-air',
        category: '技术探索',
        description: 'Hover over this card to unleash the power of CSS perspective',
        image: 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=2560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        date: '2025-07-02'
    },
    {
        id: 2,
        title: '深入理解Vue3组合式API',
        slug: 'understanding-vue3-composition-api',
        category: '技术探索',
        description: '探索Vue3组合式API的强大功能和最佳实践',
        image: 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=2560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        date: '2025-07-01'
    },
    {
        id: 3,
        title: 'Nuxt3开发实战指南',
        slug: 'nuxt3-development-guide',
        category: '技术探索',
        description: '从零开始学习Nuxt3框架开发',
        image: 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=2560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        date: '2025-06-30'
    }
];
</script>