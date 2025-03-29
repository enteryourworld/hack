'use client'

import { useEffect, useState } from 'react'

export const useScreenSize = (): { width: number; height: number } => {
	const [screenSize, setScreenSize] = useState<{
		width: number
		height: number
	}>({
		width: typeof window !== 'undefined' ? window.innerWidth : 0,
		height: typeof window !== 'undefined' ? window.innerHeight : 0
	})

	useEffect(() => {
		const handleResize = () => {
			setScreenSize({
				width: window.innerWidth,
				height: window.innerHeight
			})
		}

		window.addEventListener('resize', handleResize)
		return () => window.removeEventListener('resize', handleResize)
	}, [])

	return screenSize
}
