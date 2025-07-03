<template>
  <div
    class="fixed top-0 w-full z-50 transition-all duration-300"
    :class="[
      scrolled 
        ? 'bg-gray-800/95 backdrop-blur-sm py-4' 
        : 'bg-transparent py-6'
    ]"
  >
    <div class="max-w-7xl mx-auto px-4 flex justify-between items-center">
      <div class="text-white font-bold text-xl">Cael</div>
      <div class="flex items-center space-x-8">
        <NuxtLink to="/" class="text-white hover:text-emerald-400 transition-colors">主页</NuxtLink>
        <NuxtLink to="/category" class="text-white hover:text-emerald-400 transition-colors">分类</NuxtLink>
        <NuxtLink to="/about" class="text-white hover:text-emerald-400 transition-colors">关于</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { IInput } from "@/components/ui/input";

const scrolled = ref(false)

onMounted(() => {
  window.addEventListener('scroll', () => {
    scrolled.value = window.scrollY > 50
  })
})

onUnmounted(() => {
  window.removeEventListener('scroll', () => {
    scrolled.value = window.scrollY > 50
  })
})
</script>
