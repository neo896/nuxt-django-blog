<template>
    <div class="max-w-4xl mx-auto py-8 px-4">
        <div class="mb-8">
            <h1 class="text-4xl font-bold mb-4">{{ article?.title }}</h1>
            <div class="flex items-center gap-4 text-sm text-gray-600 dark:text-gray-400">
                <span>{{ article?.date }}</span>
                <span class="bg-emerald-100 text-emerald-700 px-2 py-1 rounded-full dark:bg-emerald-900/30 dark:text-emerald-400">
                    {{ article?.category }}
                </span>
            </div>
        </div>

        <img :src="article?.image" :alt="article?.title" class="w-full h-[400px] object-cover rounded-xl mb-8" />

        <div class="prose prose-lg dark:prose-invert max-w-none">
            <!-- 这里是文章内容的占位符 -->
            <p>{{ article?.description }}</p>
            <p>这里是文章的详细内容...</p>
        </div>
    </div>
</template>

<script lang="ts" setup>
const route = useRoute();
const router = useRouter();

// 模拟从API获取文章数据
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

const article = computed(() => {
    return articles.find(article => article.slug === route.params.slug);
});

// 如果文章不存在，重定向到首页
watchEffect(() => {
    if (!article.value) {
        router.push('/');
    }
});
</script> 